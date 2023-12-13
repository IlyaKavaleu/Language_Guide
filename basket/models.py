from django.contrib.admin import ModelAdmin
from django.db import models

from languages.models import Category
from users.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Basket {self.user}'


