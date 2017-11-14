from django.shortcuts import render
from rest_framework import generics
from modulos.albumes.models import Album
from modulos.albumes.serializers import AlbumModelSerializer
from modulos.albumes.permisions import Group_A_Permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
    permission_classes=(IsAuthenticated,Group_A_Permissions)


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
