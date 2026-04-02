from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CommentForm, IdeaForm
from .models import Comment_Model, Idea, Post_in_Python


class OnlyAuthorMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        user = self.request.user
        return (object.author == user) or user.is_superuser


class FormMixin:
    model = Idea
    form_class = IdeaForm
    template_name = 'forms/crud_idea.html'
    success_url = reverse_lazy('all_about_Python:list_idea')


# Класс для главной страницы
class HomeView(ListView):
    model = Post_in_Python
    template_name = 'python/home.html'
    context_object_name = 'posts'
    queryset = Post_in_Python.objects.filter(is_published=True)[:5]


# Класс для страницы категории
class CategoriesView(ListView):
    model = Post_in_Python
    template_name = 'python/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post_in_Python.objects.filter(
            is_published=True,
            category__id=self.kwargs['pk']
        ).select_related('category')


@login_required
def сomment_post(request, pk):
    ideas = Comment_Model.objects.filter(post__pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
    else:
        form = CommentForm()

    context = {'form': form, 'ideas': ideas, 'user': user}
    return render(request, 'forms/comments.html', context)


class PostDetailView(DetailView):
    model = Post_in_Python
    template_name = 'python/detail_post.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Post_in_Python.objects.filter(
            is_published=True,
            category__is_published=True
        )


class IdeaEditView(OnlyAuthorMixin, FormMixin, UpdateView):
    pass


class IdeaCreateView(LoginRequiredMixin, FormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date_post = timezone.now()
        response = super().form_valid(form)
        return response


class IdeaDeleteView(OnlyAuthorMixin, FormMixin, DeleteView):
    pass


class IdeaListView(ListView):
    model = Idea
    template_name = 'forms/list_idea.html'
    context_object_name = 'ideas'
    def get_queryset(self):
        return Idea.objects.order_by('-realisation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["realisation_idea"] = Idea.objects.filter(realisation=True).count()

        return context
