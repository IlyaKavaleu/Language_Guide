from django.urls import path
from . import views

app_name = 'languages'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('category/<int:id>/', views.category, name='category'),
    path('new_category/', views.new_category, name='new_category'),
    path('<int:category_id>/new_language/', views.new_language, name='new_language'),
    path('category/<int:category_id>/edit_category/', views.edit_category, name='edit_category'),
    path('language/<int:language_id>/edit_language/', views.edit_language, name='edit_language'),
    path('category/<int:category_id>/language/<int:language_id>', views.language, name='language'),
    path('categories/<int:category_id>', views.delete_category, name='delete_category'),
    path('language/<int:language_id>', views.delete_language, name='delete_language'),
    path('delete_all_categories/', views.delete_all_categories, name='delete_all_categories'),
    path('delete_all_languages/<int:language_id>', views.delete_all_languages, name='delete_all_languages'),
    path('delete_category/', views.delete_with_choose_category, name='delete_category'),

]
