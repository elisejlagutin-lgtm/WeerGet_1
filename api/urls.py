from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'ideas', views.IdeaViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
