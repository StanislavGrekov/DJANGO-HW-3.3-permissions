from rest_framework import permissions


class ForAny(permissions.BasePermission):
    """Правило для незарег.пользователей"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True


class IsOwnerORadmin(permissions.BasePermission):
    """Правило для владельцев объявлений, администраторов"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or request.user.is_staff



# class IsOwner(permissions.BasePermission):
#     """Правило для владельцев объявлений"""
#     def has_object_permission(self, request, view, obj):
#         return request.user == obj.creator
#
#
# class IsAdmin(permissions.BasePermission):
#     """Правило для администраторов"""
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_staff)


