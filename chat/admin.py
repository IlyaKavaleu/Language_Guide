from django.contrib import admin
from chat.models import Message
from django.contrib.admin import ModelAdmin


class MessageSearchAdmin(ModelAdmin):
    list_display = ['user', 'content', 'timestamp', ]
    search_fields = ['user__username', 'content', 'timestamp', ]


admin.site.register(Message, MessageSearchAdmin)
