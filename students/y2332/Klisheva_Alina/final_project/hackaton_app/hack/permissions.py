from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAbstractCaptain(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            int(request.user.role) == 1
        )


class IsCaptain(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.team.captain == request.user
        )


class IsTeamCaptain(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.captain == request.user
        )


class IsJury(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and int(request.user.role) == 2
        )


class IsSolutionOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.team == request.user.team
        )


class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request.user.role)
        print(request.user.role == 0)
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and int(request.user.role) == 0
        )


class IsMentor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            # request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and request.user.role == 1
        )
