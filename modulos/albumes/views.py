from django.shortcuts import render
from rest_framework import generics
from modulos.albumes.models import Album
from modulos.albumes.serializers import AlbumModelSerializer

# Create your views here.


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer


class DetailGenericAlbum(generics.RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer
