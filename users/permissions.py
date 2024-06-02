from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    message = "Вы не являетесь суперюзером"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsActiveUser(BasePermission):
    message = "Вы не являетесь активным сотрудником"

    def has_permission(self, request, view):
        return request.user.is_active
