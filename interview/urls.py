from django.urls import path

from . import views

app_name = 'interview'

urlpatterns = [
    path('', views.home_interview, name='home_interview'),
    path('<str:topic>/', views.topic_interview, name='topic'),
]
