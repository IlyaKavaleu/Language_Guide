from django.urls import path, include
from . import views

app_name = 'opinions'

urlpatterns = [
    path('opinions/', views.opinions, name='opinions'),
    path('add_opinion/', views.add_opinion, name='add_opinion'),
]
