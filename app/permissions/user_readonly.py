from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_authenticated:
            return True
        if request.method in [
            'POST', 'PUT', 'PATCH', 'DELETE'
        ] and (request.user.is_staff or request.user.is_superuser):
            return True
        return False
