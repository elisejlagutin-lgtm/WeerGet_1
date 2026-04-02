import pytest
from django.test import Client
from django.utils import timezone
from python.models import Post_in_Python, Category, Idea

@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Author')


@pytest.fixture
def reader(django_user_model):
    return django_user_model.objects.create(username='Reader')


@pytest.fixture
def client_reader(reader):
    client = Client()
    client.force_login(reader)
    return client


@pytest.fixture
def client_author(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def category():
    return Category.objects.create(
        title='TitleCategory',
        info='InfoCategory',
        slug='SlugCategory',
    )


@pytest.fixture
def post(category, author):
    return Post_in_Python.objects.create(
        title='TitlePost',
        info='InfoCategory',
        pub_date=timezone.now(),
        author=author,
        category=category
    )


@pytest.fixture
def idea_user(author):
    return Idea.objects.create(
        title='TitleIdea',
        description='Description',
        author=author,
        date_post=timezone.now(),
        realisation=True
    )


@pytest.fixture
def form_date_comment(author, post):
    return {
        'author': author,
        'post': post,
        'text': 'Text'
    }


@pytest.fixture
def form_date():
    return {
        'title': 'Title',
        'description':'Descr',
    }
