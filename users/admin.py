from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User


class ModelUserAdmin(ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'registered', 'country', 'city', 'age']
    search_fields = ['username', 'registered', 'country', 'city', 'age', ]


admin.site.register(User, ModelUserAdmin)
