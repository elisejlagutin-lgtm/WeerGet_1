from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    path('', include('all_about_Python.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('api.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name = 'registration/registration_form.html',
            form_class = UserCreationForm,
            success_url=reverse_lazy('all_about_Python:index'),
        ),
        name='registration'
    ),
    path('about', include('about.urls')),
    path('user/', include('user.urls')),
    path('interview/', include('interview.urls')),
    path('<slug:category_slug>/', include('all_about_Python.urls')),
]
