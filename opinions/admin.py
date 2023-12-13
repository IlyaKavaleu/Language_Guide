from django.contrib import admin
from django.contrib.admin import ModelAdmin
from opinions.models import Opinion


class ModelOpinionAdmin(ModelAdmin):
    list_display = ['user', 'text', 'rating', 'created_at', ]
    search_fields = ['user__username', 'text', 'rating', ]


admin.site.register(Opinion, ModelOpinionAdmin)
