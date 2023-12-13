from django.contrib import admin
from django.contrib.admin import ModelAdmin
from languages.models import Category, Language


class ModelLanguageAdmin(ModelAdmin):
    list_display = ['name', 'category', 'language_description', 'created', ]
    search_fields = ['name', 'description', 'category', 'created', ]

    def language_description(self, obj):
        return f'{obj.description[:20]}...' if obj.description else ''


class ModelCategoryAdmin(ModelAdmin):
    list_display = ['name', 'category_description', 'views', ]
    search_fields = ['name', 'description', 'views', ]

    def category_description(self, obj):
        return f'{obj.description[:20]}...' if obj.description else ''


admin.site.register(Category, ModelCategoryAdmin)
admin.site.register(Language, ModelLanguageAdmin)
