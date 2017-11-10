from rest_framework import viewsets
from modulos.canciones.models import Cancion
from modulos.canciones.serializers import CancionModelSerializer
# Create your views here.
"""
Django rest framework te da 3 opciones para poder hacer el CRUD
normal>generic view set (cuando no tienes un modelo) > model view sets

"""


class CancionViewSet(viewsets.ModelViewSet):
    serializer_class = CancionModelSerializer
    queryset = Cancion.objects.all() #asi todo el filtrado se hace en el web server y no en el gestor de base de datos
