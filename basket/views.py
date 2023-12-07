from django.shortcuts import render, redirect

from basket.models import Basket
from languages.models import Category
from users.models import User


def add_to_basket(request, category_id):
    category = Category.objects.get(id=category_id)
    cart = Basket.objects.create(user=request.user, category=category)
    cart.save()
    context = {'category': category}
    return redirect('languages:categories')


def delete_basket_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect('languages:index')
