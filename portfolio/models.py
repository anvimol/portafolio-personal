from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    link = models.URLField(verbose_name='Enlace', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
