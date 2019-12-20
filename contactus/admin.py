from django.contrib import admin
from .models import ContactUsInfo
# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'msg', 'created']

admin.site.register(ContactUsInfo,contactusAdmin)

