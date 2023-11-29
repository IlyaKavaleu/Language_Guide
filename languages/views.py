from django.shortcuts import render, redirect
from django.urls import reverse

from comments.models import Comments
from languages import forms
from languages.models import Category, Language


def index(request):
    return render(request, 'languages/index.html')


def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'languages/categories.html', context)


def category(request, id):
    category = Category.objects.get(id=id)
    languages = Language.objects.all().filter(category=category)
    context = {'category': category, 'languages': languages}
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
            return redirect('languages:category', id=category.id)
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
            return redirect('languages:category', id=category.id)
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


def language(request, language_id, category_id):
    language = Language.objects.get(id=language_id)
    category = language.category.id
    comments = Comments.objects.filter(language=language)
    context = {'language': language, 'category': category, 'comments':comments}
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
