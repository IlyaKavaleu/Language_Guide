from paid_card.models import PaidCard


def paid_cards(request):
    user = request.user
    return {'paid_cards': PaidCard.objects.filter(user=user) if user.is_authenticated else []}
