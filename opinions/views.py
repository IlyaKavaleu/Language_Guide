from django.contrib import messages
from django.shortcuts import render, redirect
from opinions.forms import OpinionForm
from opinions.models import Opinion
from users.models import User


def opinions(request):
    opinions = Opinion.objects.all()
    context = {'opinions': opinions}
    return render(request, 'opinions/opinions.html', context)


def add_opinion(request):
    rating = request.POST.get('rating', None)
    if request.method != 'POST':
        form = OpinionForm()
    else:
        form = OpinionForm(data=request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('opinions:opinions')
    context = {'form': form, 'rating': rating}
    return render(request, 'opinions/add_opinion.html', context)


def delete_opinion(request, opinion_id):
    opinion = Opinion.objects.get(id=opinion_id)
    if request.user == opinion.user:
        opinion.delete()
        messages.success(request, 'Отзыв успешно удален.')
    else:
        messages.error(request, 'У вас нет прав для удаления этого отзыва.')
    return redirect('opinions:opinions')
