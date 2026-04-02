from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Comment_Model, Idea
bad_words = 0

class IdeaForm(forms.ModelForm):

    class Meta():
        model = Idea
        widgets = {
            'date_post': forms.DateInput(attrs={'type': 'date'})
        }
        fields = ('title', 'description', 'realisation', 'is_published')

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()
        title = self.cleaned_data.get('title', '').strip()
        if description == title:
            return ValidationError('Описание идеи и заголовок совпадают')
        if not description:
            raise ValidationError('Информация отсутствует.')
        if len(description) <= 15:
            raise ValidationError('Описание идеи должно быть минимум 15 символов.')
        return description

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise ValidationError('Заголовок отсутствует.')
        if len(title) <= 3:
            raise ValidationError('Заголовок слишком короткий.')
        return title
   
    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        if title and description:
            if Idea.objects.filter(
                title=title,
                description=description,
            ).exists():
                raise ValidationError('Идея с таким заголовкои или описанием уже существует')
        send_mail(
            subject='New Ideas',
            message=f'Пользователь {author} опубликовал запись!',
            from_email='birthday_form@acme.not',
            recipient_list=['admin@acme.not'],
            fail_silently=True,
        )
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_Model
        fields = ('text',)
        widgets = {
            'text': forms.Textarea({'cols': '100', 'rows': '3'})
        }
