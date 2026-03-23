from django.db import models

MAX_LENGTH_TITLE = 123
from django.contrib.auth import get_user_model
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    is_published = models.BooleanField(default=True)
    info = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

User = get_user_model()


class Post_in_Python(models.Model):
    title = models.CharField("Название поста:", max_length=MAX_LENGTH_TITLE)
    is_published = models.BooleanField(default=True)
    info = models.TextField('Основная информация о посте:')
    pub_date = models.DateTimeField("Дата публикации:", null=True)
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория поста:",
    )

    def __str__(self):
        return self.title


class Comment_Model(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    post = models.ForeignKey(
        Post_in_Python,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пост",
    )
    text = models.CharField("Текст комментария", max_length=34)

    def __str__(self):
        return f"Комментарий к {self.post}"


class Model_Form(models.Model):
    title = models.CharField('Заголовок:', max_length=MAX_LENGTH_TITLE)
    is_published = models.BooleanField('Опубликовать:', default=True)
    date_post = models.DateTimeField('Дата публикации:')
    description = models.TextField('Детально о идеи:')
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    realisation = models.BooleanField(
        'Реализация:',
        default=False,
        help_text='Когда ваша идея будет реализована, поставьте галочку)')

    def __str__(self):
        return self.title
