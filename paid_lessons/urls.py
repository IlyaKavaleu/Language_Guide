from django.urls import path
from . import views

app_name = 'paid_lessons'

urlpatterns = [
    path('add_paid_lesson/<int:user_id>', views.add_paid_lesson, name='add_paid_lesson'),
    path('list_paid_lesson/<int:user_id>', views.list_paid_lesson, name='list_paid_lesson'),
    path('show_lesson/<int:lesson_id>', views.show_lesson, name='show_lesson'),
    path('add_chapter/<int:lesson_id>', views.add_chapter, name='add_chapter'),
    path('all_paid_lessons/', views.all_paid_lessons, name='all_paid_lessons'),
]


