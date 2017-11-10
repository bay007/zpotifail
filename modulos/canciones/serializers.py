from rest_framework import serializers
from modulos.canciones.models import Cancion


class CancionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ('__all__')
