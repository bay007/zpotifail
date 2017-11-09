from django.contrib import admin
from modulos.canciones.models import Cancion
# Register your models here.

class CancionesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Cancion, CancionesAdmin)
