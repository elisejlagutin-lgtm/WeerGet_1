from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Comment_Model, Model_Form


class MetalForm(forms.ModelForm):
     
    class Meta():
        model = Model_Form
        widgets = {
            'date_post': forms.DateInput(attrs={'type': 'date'})
        }
        fields = ('title', 'description', 'date_post', 'realisation', 'is_published')

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if not title:
            raise ValidationError('Поле не может быть пустым!')
        if len(title) <= 3:
            raise ValidationError('Имя пользователя слишком короткое!')
        return title
    
    def clean(self):
        super().clean()
        name = self.cleaned_data['title']
        send_mail(
            subject='New Ideas',
            message=f'Пользователь опубликовал { name } запись!',
            from_email='birthday_form@acme.not',
            recipient_list=['admin@acme.not'],
            fail_silently=True,
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_Model
        fields = ('text',)
        widgets = {
            'text': forms.Textarea({'cols': '100', 'rows': '3'})
        }
        