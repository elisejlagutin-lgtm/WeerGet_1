from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('page', views.user_page, name='user_page')
]