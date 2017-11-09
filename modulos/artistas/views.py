from django.shortcuts import render
from modulos.artistas.models import Artista
from modulos.artistas.serializers import ArtistaSerializer
from rest_framework import status
from rest_framework.response import response
from rest_framework.views import APIView

# Create your views here.
"""
por convension se pone List

esto traera todos los artistas
"""
class ListArtists(APIView):
    def get(self):
        pass

    def post(self):
        pass

"""
esto solo traera un solo artista con todos los verbos http
"""
class DetailArtist(APIView):
    def get(self):
        pass

    def put(self):
        pass
    
    def post(self):
        pass

    def delete(self):
        pass