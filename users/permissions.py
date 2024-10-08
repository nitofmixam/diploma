from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Разрешение только для владельцев"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsTeacher(BasePermission):
    """ Разрешение для учителей"""

    def has_permission(self, request, view):
        if request.user.groups.filter(name='teacher').exists():
            return True


class IsStudent(BasePermission):
    """ Разрешение для студентов"""

    def has_permission(self, request, view):
        if request.user.groups.filter(name='student').exists():
            return True
