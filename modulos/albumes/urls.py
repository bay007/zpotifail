from django.conf.urls import url
from modulos.albumes.views import ListGenericAlbum, DetailGenericAlbum

urlpatterns = [
    url(r'^albumes/$', ListGenericAlbum.as_view(), name="listAlbumes"),
    url(r'^albumes/(?P<pk>[0-9a-f-])/$',DetailGenericAlbum.as_view(), name="detailAlbumes"),
]