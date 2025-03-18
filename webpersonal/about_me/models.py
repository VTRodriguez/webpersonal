from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='título');
    description = models.TextField(verbose_name='descripción');
    image = models.ImageField(verbose_name='imagen', upload_to='projects');
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación');
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de edición');

    class Meta:
        verbose_name = 'estudio'
        verbose_name_plural = 'estudios'
        ordering = ['-created']

    def __str__(self):
        return self.title
