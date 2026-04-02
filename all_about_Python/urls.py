from django.urls import path

from . import views

app_name = 'all_about_Python'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list_idea', views.IdeaListView.as_view(), name = 'list_idea'),
    path('create', views.IdeaCreateView.as_view(), name = 'idea_create'),
    path('<int:pk>/comment', views.сomment_post, name='comment_create'),
    path('<int:pk>/edit/', views.IdeaEditView.as_view(), name='idea_edit'),
    path('<int:pk>/delete/', views.IdeaDeleteView.as_view(), name='idea_delete'),
    path('<int:pk>/post', views.PostDetailView.as_view(), name='detail_post'),
    path('<int:pk>/category', views.CategoriesView.as_view(), name='categories'),
]
