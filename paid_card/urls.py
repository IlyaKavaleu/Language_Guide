from django.urls import path
from . import views

app_name = 'paid_card'

urlpatterns = [
    path('add_to_paid_card/<int:paid_lesson_id>/', views.add_to_paid_card, name='add_to_paid_card'),
    path('delete_paid_card/<int:paid_card_id>/', views.delete_paid_card, name='delete_paid_card'),
]
