from rest_framework import serializers
from modulos.artistas.models import Artista

"""
Se deben usar cuando no se deba guardar ese resultado y se ocupe algo para validar cosas
ej endpoint que pase precio y descuento y al final debe regresar el precio con decuento para evitar casteos y demas 
creamos el serializer especifico que pase el decimal fields para el precio y el decuento y al final el serializer lo debe convertir a decimal y validar que haya casteo


class ArtistaSerializer(serializers.Serializer):
    name = models.CharField(max_length=length, ${blank=True, null=True})
    .
    .
    .
"""


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ('__all__')
