from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'bio')