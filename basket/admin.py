from django.contrib import admin
from django.contrib.admin import ModelAdmin
from basket.models import Basket


class ModelBasketAdmin(ModelAdmin):
    list_display = ['user', 'category', ]
    search_fields = ['user__username', ]


admin.site.register(Basket, ModelBasketAdmin)
