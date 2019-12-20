from django.contrib import admin
from .models import property, images
# Register your models here.


admin.site.site_header = 'REIMGN'                    # default: "Django Administration"
admin.site.index_title = 'REIMGN Administration'                 # default: "Site administration"

class propertyAdmin(admin.ModelAdmin):
    list_display = ['location', 'zip']

class imagesAdmin(admin.ModelAdmin):
    list_display = ['property', 'image']

admin.site.register(property,propertyAdmin)
admin.site.register(images,imagesAdmin)