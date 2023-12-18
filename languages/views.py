from django.core import paginator
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comments.forms import CommentForm
from comments.models import Comments
from languages import forms
from languages.models import Category, Language


def index(request):
    return render(request, 'languages/index.html')


def categories(request):
    categories_list = Category.objects.all()
    categories_per_page = 9
    paginator = Paginator(categories_list, categories_per_page)
    page = request.GET.get('page')
    try:
        categories_page = paginator.page(page)
    except PageNotAnInteger:
        categories_page = paginator.page(1)
    except EmptyPage:
        categories_page = paginator.page(paginator.num_pages)

    context = {'categories_page': categories_page}
    return render(request, 'languages/categories.html', context)


def all_languages(request, category_id):
    category_id = Category.objects.get(id=category_id)
    languages_list = Language.objects.filter(category=category_id).order_by('created')
    languages_per_page = 3
    paginator = Paginator(languages_list, languages_per_page)
    page = request.GET.get('page')
    try:
        languages_page = paginator.page(page)
    except PageNotAnInteger:
        languages_page = paginator.page(1)
    except EmptyPage:
        languages_page = paginator.page(paginator.num_pages)
    list_languages = Language.objects.all()
    context = {'languages_page': languages_page}
    return render(request, 'languages/all_languages.html', context)


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.increment_views()
    context = {'category': category}
    return render(request, 'languages/category.html', context)


def new_category(request):
    if request.method != 'POST':
        form = forms.CategoryForm()
    else:
        form = forms.CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('languages:categories')
    context = {'form': form}
    return render(request, 'languages/new_category.html', context)


def new_language(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        form = forms.LanguageForm()
    else:
        form = forms.LanguageForm(request.POST, request.FILES)
        if form.is_valid():
            new_lang = form.save(commit=False)
            new_lang.category = category
            new_lang.save()
            return redirect('languages:category', category_id=category.id)
    context = {'category': category, 'form': form}
    return render(request, 'languages/new_language.html', context)


def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        form = forms.CategoryForm(instance=category)
    else:
        form = forms.CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('languages:category', category_id=category.id)
    context = {'category': category, 'form': form}
    return render(request, 'languages/edit_category.html', context)


def edit_language(request, language_id):
    language = Language.objects.get(id=language_id)
    if request.method != 'POST':
        form = forms.LanguageForm(instance=language)
    else:
        form = forms.LanguageForm(request.POST, request.FILES, instance=language)
        if form.is_valid():
            form.save()
            return redirect('languages:category', language.category.id)
    context = {'language': language, 'form': form}
    return render(request, 'languages/edit_language.html', context)


def language(request, category_id, language_id):
    language = Language.objects.get(id=language_id)
    category = language.category.id
    comments = Comments.objects.filter(language=language)
    commentForm = CommentForm()
    context = {'language': language, 'category': category, 'comments': comments, 'commentForm': commentForm}
    return render(request, 'languages/language.html', context)


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('languages:categories')


def delete_language(request, language_id):
    language = Language.objects.get(id=language_id)
    language.delete()
    return redirect('languages:category', id=language.category.id)


def delete_all_categories(request):
    categories = Category.objects.all()
    categories.delete()
    return redirect('languages:categories')


def delete_all_languages(request, category_id):
    languages = Category.objects.all()
    languages.delete()
    return redirect('languages:categories', id=category.id)


def delete_with_choose_category(request):
    template_name = 'languages/categories.html'  # Замените на ваш шаблон
    model = Category  # Замените на вашу модель данных
    category_id = request.POST.get('category_id')  # Получаем ID категории из формы
    try:
        category = model.objects.get(pk=category_id)
        category.delete()  # Удаляем категорию из базы данных
    except model.DoesNotExist:
        pass  # Обработка случая, когда категория не найдена
    return redirect('languages:categories')


def choose_studies(request):
    return render(request, 'languages/choose_studies.html')