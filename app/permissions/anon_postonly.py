from rest_framework.permissions import BasePermission


class IsAuthenticatedOrPostOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'PUT', 'PATCH', 'UPDATE'] and request.user.is_authenticated:
            return True
        if request.method == 'POST' and request.user.is_authenticated is False:
            return True
        return False
