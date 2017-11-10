from rest_framework import serializers
from modulos.albumes.models import Album


#Se debe especificar que es de tipo MODEL, si no la vista retornara vacio
class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('__all__')