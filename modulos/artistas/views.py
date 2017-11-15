from django.shortcuts import get_object_or_404
from modulos.artistas.models import Artista
from modulos.artistas.serializers import ArtistaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from modulos.artistas.permissions import Group_B_Permissions
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope,TokenHasScope

# Create your views here.
"""
por convension se pone List

esto traera todos los artistas
"""


class ListArtistas(APIView):
    permission_classes=(IsAuthenticated,TokenHasReadWriteScope,)
    def get(self, request):
        artistas_db = Artista.objects.all()  # obtenemos todos los artistas
        artistas_para_mandar_a_la_vista = ArtistaSerializer(
            artistas_db, many=True)  # retorna lo que te pase en una lista
        return Response(artistas_para_mandar_a_la_vista.data, status=status.HTTP_200_OK)

    def post(self, request):
        artista_desde_cliente = ArtistaSerializer(data=request.data)
        if artista_desde_cliente.is_valid():
            artista_desde_cliente.save()
            return Response(artista_desde_cliente.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(artista_desde_cliente.errors,
                            status=status.HTTP_400_BAD_REQUEST)


"""
esto solo traera un solo artista con todos los verbos http
"""


class DetailArtistas(APIView):
    def get(self, request, identificador):
        artista = get_object_or_404(Artista, pk=identificador)
        artista_para_la_vista = ArtistaSerializer(artista)
        return Response(artista_para_la_vista.data, status.HTTP_200_OK)

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
