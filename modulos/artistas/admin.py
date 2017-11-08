from django.contrib import admin
from modulos.artistas.models import Artista
# Register your models here.


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Artista, ArtistaAdmin)
