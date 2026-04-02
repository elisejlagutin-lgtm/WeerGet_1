from rest_framework import permissions


class IsAuthorOrReadOnlu(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False