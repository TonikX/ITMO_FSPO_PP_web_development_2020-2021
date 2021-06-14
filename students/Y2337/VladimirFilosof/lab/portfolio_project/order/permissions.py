from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    The request is admin a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsAuthenticatedOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.user)
        return bool(
            request.user and request.user.is_authenticated and request.user == obj.user
        )
