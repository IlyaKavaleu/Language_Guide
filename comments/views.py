from django.shortcuts import render, redirect
from django.urls import reverse

from languages.models import Language
from .models import Comments
from .forms import CommentForm


def add_comment_to_language(request, language_id):
    language = Language.objects.get(id=language_id)
    category_id = language.category.id
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.language = language
            comment.user = request.user
            comment.save()
            return redirect('languages:language', language_id=language.id, category_id=category_id)
    context = {'form': form, 'language': language}
    context = {'form': form, 'language': language}
    return render(request, 'comments/add_comment_to_language.html', context)
