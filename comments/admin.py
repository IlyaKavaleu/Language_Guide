from django.contrib import admin
from django.contrib.admin import ModelAdmin
from comments.models import Comments


class ModelCommentAdmin(ModelAdmin):
    list_display = ['user', 'language', 'text', 'created_at', ]
    search_fields = ['user__username', 'text', ]


admin.site.register(Comments, ModelCommentAdmin)

