from django.db import models

from paid_lessons.models import PaidLesson
from users.models import User
from paid_card.models import PaidCard


class Order(models.Model):
    CREATED = 0
    PAID = 1
    STATUSES = (
        (CREATED, 'Created'),
        (PAID, 'Paid'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    paid_card_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)  # WYBORKA
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        paid_cards = PaidCard.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.paid_card_history = {
            'purchased_items': [paid_card.de_json() for paid_card in paid_cards],
            'total_sum': float(paid_cards.price_all_products()),
        }
        paid_cards.delete()
        self.save()
