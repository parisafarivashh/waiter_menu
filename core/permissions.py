from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff is True:
            return True
        return False

