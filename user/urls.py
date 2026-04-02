from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('send/<int:recipient_id>/', views.user_send_message, name='send_message'),
    path('read_my_message/', views.user_receiving_message, name='read_message'),
    path('<int:user_id>/', views.user_page, name='user_page')
]