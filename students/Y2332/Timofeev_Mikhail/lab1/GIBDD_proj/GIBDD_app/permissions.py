from rest_framework.permissions import *


PERMS_MAP = {
    'GET': 'view_',
    'DELETE': 'delete_',
    'PATCH': 'change_',
    'POST': 'add_',
    'PUT': 'change_'
}


class UserViewPermissions(BasePermission):

    def has_permission(self, request, view):
        app_label = view.queryset.model._meta.app_label
        model_name = view.queryset.model._meta.model_name

        return request.user.has_perm(str(app_label+'.'+PERMS_MAP[request.method]+model_name)) or \
            request.user.is_superuser
