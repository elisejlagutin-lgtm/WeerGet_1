from django.urls import path

from . import views


app_name = 'all_about_Python'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.IdeaListView.as_view(), name = 'list'),
    path('create', views.Form_Create_View.as_view(), name = 'my_form_create'),
    path('<int:pk>/comment', views.Comment_Post, name='comment_create'),
    path('<int:pk>/edit/', views.Form_Edit_View.as_view(), name='my_form_edit'),
    path('<int:pk>/delete/', views.Form_Delete_View.as_view(), name='my_form_delete'),
    path('<int:pk>/post', views.PostDetailView.as_view(), name='detail_post'),
    path('<int:pk>/category', views.Categories_View.as_view(), name='categories'),
]
