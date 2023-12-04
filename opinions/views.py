from django.shortcuts import render, redirect

from opinions.forms import OpinionForm
from opinions.models import Opinion
from users.models import User


def opinions(request):
    opinions = Opinion.objects.all()
    context = {'opinions': opinions}
    return render(request, 'opinions/opinions.html', context)


def add_opinion(request):
    if request.method != 'POST':
        form = OpinionForm()
    else:
        form = OpinionForm(data=request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('opinions:opinions')
    context = {'form': form}
    return render(request, 'opinions/add_opinion.html', context)