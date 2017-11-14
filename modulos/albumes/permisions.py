from rest_framework.permissions import BasePermission
from modulos.usuarios.models import Usuario
from django.contrib.auth.models import Group


class Group_A_Permissions(BasePermission):
    # si el usuario existe en el grupo devuelve true, de otro modo false
    def _is_in_group(self, group_name, user):
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()

    def has_permission(self, request, view):
        if self._is_in_group("grupo_a", request.user):
            return True
        return False
