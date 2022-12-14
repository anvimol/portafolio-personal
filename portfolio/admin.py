from django.contrib import admin
from .models import Project

# Register your models here.
# Necedario para poder ver los campos Creaded, Updated
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
