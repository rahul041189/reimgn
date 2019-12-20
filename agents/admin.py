from django.contrib import admin
from .models import agents
# Register your models here.

class agentsAdmin(admin.ModelAdmin):
    list_display = ['lname', 'email', 'created']

admin.site.register(agents,agentsAdmin)

