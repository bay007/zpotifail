from django.conf.urls import url
from modulos.artistas.views import ListArtistas, DetailArtistas
urlpatterns = [

    url(r'^artistas/$', ListArtistas.as_view(), name="listArtistas"),
    url(r'^artistas/(?P<identificador>[0-9a-f-]+)/$', DetailArtistas.as_view(), name="detailArtistas"),
]
