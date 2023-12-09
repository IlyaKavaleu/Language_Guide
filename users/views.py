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


def get_inst(request):
    instagram_username = request.user.instagram if request.user.instagram else None
    if instagram_username:
        main_address = 'https://www.instagram.com/'
        full_address = main_address + instagram_username + '/'
    else:
        full_address = None
    return full_address


def get_facebook(request):
    facebook_username = request.user.facebook if request.user.facebook else None
    # name = ''.join(facebook_username).replace(' ', '.').lower()
    if facebook_username:
        main_address = 'https://www.facebook.com/'
        full_address = main_address + facebook_username + '/'
    else:
        full_address = None
    return full_address


def account(request):
    user = User.objects.get(id=request.user.id)
    full_address_instagram = get_inst(request)
    full_address_facebook = get_facebook(request)
    baskets = Basket.objects.filter(user=user)
    context = {'user': user, 'baskets': baskets, 'full_address_instagram': full_address_instagram,
               'full_address_facebook': full_address_facebook}
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


