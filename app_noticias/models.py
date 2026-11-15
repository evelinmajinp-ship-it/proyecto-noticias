from django.db import models


class Noticia(models.Model):

    titulo = models.CharField(max_length=200)

    fecha_ocurrencia = models.DateField()

    lugar = models.CharField(max_length=150)

    descripcion = models.TextField()

    imagen = models.ImageField(upload_to='noticias/')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha_ocurrencia']