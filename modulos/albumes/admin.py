from django.contrib import admin
from modulos.albumes.models import Album
# Register your models here.

class AlbumesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Album,AlbumesAdmin)
