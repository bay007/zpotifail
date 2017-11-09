from django.conf.urls import url
from modulos.artistas.views import ListArtistas
urlpatterns = [

    url(r'^artistas/', ListArtistas.as_view(), name="listArtistas"),
]
