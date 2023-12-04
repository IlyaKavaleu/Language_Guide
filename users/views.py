from basket.models import Basket
from programming_guide.settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserEditForm, ExtendedUserCreationForm
from users.models import User


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
    baskets = Basket.objects.filter(user=user)
    context = {'user': user, 'baskets': baskets}
    return render(request, 'registration/account.html', context)


def edit_account(request):
    user = User.objects.get(username=request.user)
    if request.method != 'POST':
        form = UserEditForm(instance=user)
    else:
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('languages:index')
    context = {'user': user, 'form': form}
    return render(request, 'registration/edit_account.html', context)
