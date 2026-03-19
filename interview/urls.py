from django.urls import path

from . import views

app_name = 'interview'

urlpatterns = [
    path('interview/', views.home_interview, name='home_interview'),
    path('interview/<str:topic>/', views.topic_interview, name='topic'),
    path('interview/<int:pk>/', views.task_topic, name='task')
]
