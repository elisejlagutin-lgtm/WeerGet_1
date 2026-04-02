from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Message, GroupsUser
from .forms import MessageCreate

from python.models import Idea

User = get_user_model()


@login_required
def user_page(request, user_id):
    not_read_messages = Message.objects.filter(
        recipient=user_id,
        is_read=False).count()
    context = {
        'user': User.objects.get(pk=user_id),
        'posts_user': Idea.objects.filter(author = user_id),
        'NoReadMessages': not_read_messages
    }
    return render(request, 'user/user_page.html', context)


@login_required
def user_send_message(request, recipient_id):
    recipient = User.objects.get(pk=recipient_id)
    anonymous = User.objects.get(username='anonymous')
    if request.user.id == recipient_id:
        messages = Message.objects.filter(recipient=recipient)
    else:
        messages = Message.objects.filter(
            recipient=recipient,
            sender=request.user)
    if request.method == 'POST':
        form = MessageCreate(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if message.is_anonymous:
                message.sender = anonymous
            else:
                message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('user:user_page', recipient_id)
    else:
        form = MessageCreate()

    context = {'form': form, 'messages': messages}
    return render(request, 'user/send_message.html', context)


@login_required
def user_receiving_message(request):
    messages = Message.objects.filter(recipient = request.user)
    context = {'messages': messages}
    return render(request, 'user/reading_message.html', context)
