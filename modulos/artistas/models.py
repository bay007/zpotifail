from django.db import models
import uuid
from modulos.albumes.models import Album

# Create your models here.


class Artista(models.Model):  # debe ser en plural la clase
    GENEROS = (
        ('pop','Pop'),
        ('electronica','Electrónica'),
        ('jazz','Jazz'),
        ('clasica','Clásica'),
        ('ranchero','Ranchero'),
    )

    # checar por que uuid no se llama cono funcion
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.URLField()
    # Si se quiere METER ATRIBUTOs en la tablal intermedia ahi si habria que hacerla a mano
    albums = models.ManyToManyField(Album)
    is_band = models.BooleanField(default=False)
    genero_primario = models.CharField(max_length=100, choices=GENEROS)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return
