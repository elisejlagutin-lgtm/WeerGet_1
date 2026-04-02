from rest_framework import viewsets
from python.models import Idea
from .serializer import IdeaSerializer
from django.utils import timezone
from .permissions import IsAuthorOrReadOnlu


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsAuthorOrReadOnlu,)
    throttle_classes = 'low_request'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, date_post=timezone.now())
