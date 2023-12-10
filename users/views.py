from django.urls import reverse
from programming_guide.settings import DEFAULT_FROM_EMAIL

from basket.models import Basket
from programming_guide.settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserEditForm, ExtendedUserCreationForm
from users.models import User
from django.core.mail import send_mail


def send_email(subject, message, recipient_list):
    send_mail(subject, message, 'kavaleuilia@gmail.com', recipient_list)


def register(request):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за регистрацию. Мы рады видеть вас в нашем сообществе.'

    if request.method != 'POST':
        form = ExtendedUserCreationForm()
    else:
        form = ExtendedUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            recipient_list = [new_user.email]
            send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)
            return redirect(reverse('languages:index'))
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


def get_linkedin(request):
    linkedin_username = request.user.linkedin if request.user.linkedin else None
    # name = ''.join(facebook_username).replace(' ', '.').lower()
    if linkedin_username:
        main_address = 'https://www.linkedin.com/in/'
        full_address = main_address + linkedin_username + '/'
    else:
        full_address = None
    return full_address


def account(request):
    user = User.objects.get(id=request.user.id)
    email = user.email
    full_address_instagram = get_inst(request)
    full_address_facebook = get_facebook(request)
    full_address_linkedin = get_linkedin(request)
    baskets = Basket.objects.filter(user=user)
    context = {'user': user, 'email': email, 'baskets': baskets,
               'full_address_instagram': full_address_instagram,
               'full_address_facebook': full_address_facebook,
               'full_address_linkedin': full_address_linkedin,
               }
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


