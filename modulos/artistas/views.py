from django.shortcuts import get_object_or_404
from modulos.artistas.models import Artista
from modulos.artistas.serializers import ArtistaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from modulos.artistas.permissions import Group_B_Permissions
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Create your views here.
"""
por convension se pone List

esto traera todos los artistas
"""


class ListArtistas(APIView):
    #permission_classes = (IsAuthenticated, Group_B_Permissions)

    def _filterring(self, params):
        genero = params.get("genero", "")
        nombre = params.get("nombre", "")
        is_band = False if params.get("is_band", "-").lower()=="true" else True
        print(is_band)

        queryset = artistas = Artista.objects.filter((Q(genero_primario__iexact=genero) & Q(nombre__icontains=nombre))|Q(is_band=is_band))
        print(queryset.query.__str__())
        return queryset

    def get(self, request):
        
        if request.query_params:
            print(request.query_params)
            artistas_db=self._filterring(request.query_params)
        else:
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
