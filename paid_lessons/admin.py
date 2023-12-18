from django.contrib import admin
from paid_lessons.models import PaidLesson, PaidСhapter


class PaidLessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration', 'date_published', 'teacher', ]
    search_fields = ['title', 'price', 'duration', 'date_published', 'teacher__username', ]


admin.site.register(PaidLesson, PaidLessonAdmin)
admin.site.register(PaidСhapter)
