from django.urls import reverse
from python.forms import CommentForm, IdeaForm


# Тест на порядок идей
def test_order_ideas():
    pass


# Тест на то что зарегистрированный пользователь может оставить комментарий
def test_form_create_comment(form_date_comment, post, client_reader):
    url = reverse('all_about_Python:comment_create', args=(post.id,))
    response = client_reader.get(url, data=form_date_comment)
    form_in_context = 'form' in response.context
    assert form_in_context is True
    isinstance(response.context['form'], CommentForm)


# Тест на то что зарегистрированный пользователь может оставить идею.
def test_form_create_idea_by_reader(form_date, client_reader):
    url = reverse('all_about_Python:idea_create')
    response = client_reader.get(url, data=form_date)
    form_in_context = 'form' in response.context
    assert form_in_context is True
    isinstance(response.context['form'], IdeaForm)
