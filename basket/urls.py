from django.urls import path, include
from . import views

app_name = 'basket'

urlpatterns = [
    path('add_to_basket/<int:category_id>', views.add_to_basket, name='add_to_basket'),
]
