from django import forms
from .models import Message


class MessageCreate(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)