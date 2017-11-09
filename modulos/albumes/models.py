from django.db import models
import uuid
from django.conf import settings
# Create your models here.



class Album(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nombre = models.CharField(max_length=80)
    cover = models.URLField()
    fecha_lanzamiento = models.DateField()
    copyright = models.CharField(max_length=100)
    numero_canciones = models.IntegerField()
    genero = models.CharField(max_length=50)
    pais = models.CharField(max_length=50, choices=settings.PAISES)

    def __str__(self):
        return

    def __unicode__(self):
        return
