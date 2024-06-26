import stripe
from django.http import HttpResponse
from http import HTTPStatus
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from stripe.error import SignatureVerificationError
from orders.models import Order
from programming_guide.settings import DOMAIN_NAME, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
from paid_card.models import PaidCard
from orders.forms import OrderForm

stripe.api_key = STRIPE_SECRET_KEY


class SuccessTemplateView(TemplateView):
    template_name = 'orders/success.html'
    title = 'Thank you for order'


class CanceledTemplateView(TemplateView):
    template_name = 'orders/canceled.html'


class OrderListView(ListView):
    template_name = 'orders/orders.html'
    title = 'PrGuide - Orders'
    queryset = Order.objects.all()
    ordering = ('-created')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class OrderDetailView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - Order #{self.object.id}'
        return context


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Create order'

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        paid_cards = PaidCard.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=paid_cards.stripe_products(),
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(DOMAIN_NAME, reverse('orders:order_canceled'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user  # form -> method OBJECT instance -> our initiator -> taken OUR request.user
        return super(OrderCreateView, self).form_valid(form)  # edit method super, override super for our class


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = event['data']['object']
        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()

