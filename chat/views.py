# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm


@login_required
def chat_room(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat:chat_room')
    return render(request, 'chat/chat_room.html', {'messages': messages, 'form': form})
