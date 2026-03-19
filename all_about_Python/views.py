from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CommentForm, MetalForm
from .models import Comment_Model, Model_Form, Post_in_Python
from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyAuthorMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class FormMixin:
    model = Model_Form
    form_class = MetalForm
    template_name = 'forms/form_ideas.html'
    context_object_name = 'form'
    success_url = reverse_lazy('all_about_Python:list')

# Класс для главной страницы
class IndexView(ListView):
    model = Post_in_Python
    template_name = 'python/index.html'
    context_object_name = 'posts'
    queryset = Post_in_Python.objects.filter(is_published=True)[:5]

# Класс для страницы категории
class Categories_View(ListView):
    model = Post_in_Python
    template_name = 'python/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post_in_Python.objects.filter(
            is_published=True,
            category__id=self.kwargs['pk']
        )


@login_required
def Comment_Post(request, pk):
    ideas = Comment_Model.objects.filter(post__pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
            return redirect('all_about_Python:index')
    else:
        form = CommentForm()
    
    context = {'form': form, 'ideas': ideas, 'user': user}
    return render(request, 'forms/form_comment.html', context)


class PostDetailView(DetailView):
    model = Post_in_Python
    template_name = 'python/detail.html'
    context_object_name = 'details'

    def get_queryset(self):
        return Post_in_Python.objects.filter(
            is_published=True,
            category__is_published=True
        )


class Form_Edit_View(OnlyAuthorMixin, FormMixin, UpdateView):
    pass


class Form_Create_View(LoginRequiredMixin, FormMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response

class Form_Delete_View(OnlyAuthorMixin, FormMixin, DeleteView):
    pass


class ListView(ListView):
    model = Model_Form
    template_name = 'forms/list.html'
    context_object_name = 'ideas'
    def get_queryset(self):
        return Model_Form.objects.order_by('-date_post')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["realisation_idea"] = Model_Form.objects.filter(realisation=True).count()
        return context
    
