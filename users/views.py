from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserEditForm, ExtendedUserCreationForm


def register(request):
    if request.method != 'POST':
        form = ExtendedUserCreationForm()
    else:
        form = ExtendedUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('languages:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def account(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, 'registration/account.html', context)


def edit_account(request):
    user = User.objects.get(username=request.user)
    if request.method != 'POST':
        form = UserEditForm(instance=user)
    else:
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('languages:index')
    context = {'user': user, 'form': form}
    return render(request, 'registration/edit_account.html', context)
