from django.contrib import admin
from .models import Project
from .models import Hobby

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Hobby, ProjectAdmin)