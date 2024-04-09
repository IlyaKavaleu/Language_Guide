from django.db import models

from paid_lessons.models import PaidLesson
from programming_guide.settings import AUTH_USER_MODEL


class PaidCardQuerySet(models.QuerySet):
    def price_all_products(self):
        return sum([paid_card.sum() for paid_card in self])

    def sum_all_products(self):
        return len([paid_card for paid_card in self])

    def stripe_products(self):
        line_items = []
        for paid_card in self:
            item = {
                'price': paid_card.paid_lesson.stripe_product_price_id,
                'quantity': paid_card.quantity,
            }
            line_items.append(item)
        return line_items


class PaidCard(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid_lesson = models.ForeignKey(PaidLesson, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = PaidCardQuerySet.as_manager()

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт: {self.paid_lesson.title}"

    def sum(self):
        return self.paid_lesson.price * self.quantity

    def de_json(self):
        paid_card_item = {
            'paid_lesson_name': self.paid_lesson.title,
            'quantity': self.quantity,
            'price': float(self.paid_lesson.price),
            'sum': float(self.sum())
        }
        return paid_card_item
