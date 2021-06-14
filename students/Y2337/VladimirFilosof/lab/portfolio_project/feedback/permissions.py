from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOwnerOrReadOnly(BasePermission):
    """
    The request is admin a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated and obj.user == request.user
        )

