from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.shortcuts import render

from all_about_Python.models import Model_Form

User = get_user_model()

#class UserPageView(ListView):
#    model = User
#    template_name = 'user/user_page.html'
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['posts_user'] = Post_in_Python.objects.filter(
#            author = self.request.user
#        )
#        return context


def user_page(request):
    current_user = request.user
    context = {
        'user': current_user,
        'posts_user': Model_Form.objects.filter(
            author = current_user
        )
    }
    return render(request, 'user/user_page.html', context)