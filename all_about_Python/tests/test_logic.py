from django.urls import reverse
import pytest
from all_about_Python.models import Model_Form, Comment_Model


def test_create_idea_by_client_reader(client_reader):
    initial_count = Model_Form.objects.count()

    url = reverse('all_about_Python:my_form_create')
    form_data = {
        'title': 'Test Idea',
        'description': 'Test description',
        'date_post': '2023-12-31',
        'realisation': 'In progress',
        'is_published': True,
    }
    response = client_reader.post(url, data=form_data)
    assert Model_Form.objects.count() == (initial_count + 1)


def test_create_idea_by_anonumos(db, client):
    initial_count = Model_Form.objects.count()

    url = reverse('all_about_Python:my_form_create')
    form_data = {
        'title': 'Test Idea',
        'description': 'Test description',
        'date_post': '2023-12-31',
        'realisation': 'In progress',
        'is_published': True,
    }
    response = client.post(url, data=form_data)
    assert Model_Form.objects.count() == initial_count


def test_delete_idea_by_author(db, client_author, idea_user):
    initial_count = Model_Form.objects.count()
    url = reverse('all_about_Python:my_form_delete', args=(idea_user.id,))
    response = client_author.delete(url)
    assert Model_Form.objects.count() == (initial_count - 1)


#def test_edit_idea_by_author(client_author, idea_user, form_date):
#    url = reverse('all_about_Python:my_form_edit', args=(idea_user.id,))
#    response = client_author.post(url, data=form_date)
#    updated_idea = Model_Form.objects.get(pk=idea_user.id)
#    assert updated_idea.title == form_date['title']
#    assert updated_idea.description == form_date['description']


def test_add_comment_by_client(db, post, client, form_date_comment):
    initial_count = Comment_Model.objects.count()
    url = reverse('all_about_Python:comment_create', args=(post.id,))
    response = client.post(url, data=form_date_comment)
    comment = Comment_Model.objects.last()
    assert initial_count == Comment_Model.objects.count() - 1
