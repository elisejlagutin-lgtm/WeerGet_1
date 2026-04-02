from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_messages')
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipient')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Добавь поле реального автора чтобы тот человек который поставил себя анонимом мог потом посмотреть свое сообщение

class GroupsUser(models.Model):
    participant = models.ManyToManyField(User)
    name_group = models.CharField(max_length=25)
