from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageCreate

from all_about_Python.models import Model_Form

User = get_user_model()


def user_page(request, user_id):
    context = {
        'user': User.objects.get(pk=user_id),
        'posts_user': Model_Form.objects.filter(
            author = user_id
        )
    }
    return render(request, 'user/user_page.html', context)


# Тут будет функция для отправки сообщения
def user_send_message(request, recipient_id):
    recipient = User.objects.get(pk=recipient_id)
    if request.method == 'POST':
        form = MessageCreate(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('user:user_page', recipient_id)
    else:
        form = MessageCreate()

    context = {'form': form}
    return render(request, 'user/send_message.html', context)


# Тут будет функция для получения сообщения
def user_receiving_message(request):
    messages = Message.objects.filter(recipient = request.user)
    context = {'messages': messages}
    return render(request, 'user/reading_message.html', context)