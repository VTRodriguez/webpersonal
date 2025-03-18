from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    image = models.ImageField(verbose_name='imagen', upload_to='projects')
    started = models.DateField(verbose_name='fecha de inicio')
    finished = models.DateField(verbose_name='fecha de finalización', null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de edición')

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_finished_display(self):
        return self.finished.strftime('%d/%m/%Y') if self.finished else 'Actualidad'