from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('my_account/', views.account, name='my_account'),
    path('edit_account/', views.edit_account, name='edit_account'),
]
