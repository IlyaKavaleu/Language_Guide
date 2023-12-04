from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'first_name', 'last_name', 'email', 'image', ]


admin.site.register(User)
