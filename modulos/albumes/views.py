from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from modulos.albumes.models import Album
from modulos.albumes.serializers import AlbumModelSerializer
from modulos.albumes.permisions import Group_A_Permissions
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes=(IsAuthenticated,Group_A_Permissions)
    filter_fields=("pais","numero_canciones",)


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
