from django.urls import reverse
from http import HTTPStatus
import pytest

# Тест на то что анонимный юзер может попасть на страницы с идеями, созданием идеи, главной страницей.
@pytest.mark.parametrize(
    'name, status',
    (
        ('all_about_Python:list_idea', HTTPStatus.OK),
        ('all_about_Python:idea_create', HTTPStatus.FOUND),
        ('all_about_Python:home', HTTPStatus.OK),
    )
)
def test_anonumos_user(db, name, status, client):
    url = reverse(name)
    response = client.get(url)
    assert response.status_code == status


# Тут проверяется доступ страниц с pk для анонимного пользователя.
@pytest.mark.parametrize(
    'name, pk',
    (
        ('all_about_Python:categories', pytest.lazy_fixture('category')),
        ('all_about_Python:detail_post', pytest.lazy_fixture('post')),
    )
)
def test_item_routes_anonumos(db, name, client, pk):
    url = reverse(name, args=(pk.id,))
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


# Тут проверяется доступность страниц редактирования и удаления идеи для автора.
@pytest.mark.parametrize(
    'name',
    (
        ('all_about_Python:idea_edit'),
        ('all_about_Python:idea_delete'),
    )
)
def test_author_response(name, idea_user, client_author):
    url = reverse(name, args=(idea_user.id,))
    if name == 'all_about_Python:idea_edit':
        response = client_author.post(
            url,
            data={
                'title': 'Test Title',
                'description': 'Test Description',
                'date_post': '2023-01-01',
                'realisation': True,
                'is_published': True
            }
        )
    else:
        response = client_author.delete(url)
    assert response.status_code == HTTPStatus.FOUND


# Тут проверяется доступность страниц редактирования и удаления идеи для читателя.
@pytest.mark.parametrize(
    'name',
    (
        ('all_about_Python:idea_edit'),
        ('all_about_Python:idea_delete'),
    )
)
def test_reader_response(name, idea_user, client_reader):
    url = reverse(name, args=(idea_user.id,))
    if name == 'all_about_Python:idea_edit':
        response = client_reader.post(
            url,
            data={
                'title': 'Test Title',
                'description': 'Test Description',
                'date_post': '2023-01-01',
                'realisation': True,
                'is_published': True
            }
        )
    else:
        response = client_reader.delete(url)
    assert response.status_code == HTTPStatus.FORBIDDEN


# Тут проверяется доступ страницы создания комментария для незаригестрированного пользователя.
def test_create_comment_routes(db, client, post, form_date_comment):
    url = reverse('all_about_Python:comment_create', args=(post.id,))
    response = client.post(url, data=form_date_comment)
    assert response.status_code == HTTPStatus.FOUND
