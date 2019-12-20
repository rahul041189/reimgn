from django.shortcuts import render
from .models import property, images
from agents.models import agents
from django.views.decorators.gzip import gzip_page
# Create your views here.

@gzip_page
def index(request):
    properties = property.objects.all().order_by('-is_featured')
    property_images = images.objects.all()
    context = {'properties': properties, 'property_images': property_images}
    return render(request, 'home/index.html', context)


def show_property(request, id):
    ppt_display = property.objects.get(pk=id)
    ppt_imgs = ppt_display.images_set.all()
    context = {'ppt_display': ppt_display, 'ppt_imgs':ppt_imgs}
    return render(request, 'home/show_property.html', context)


@gzip_page
def terms(request):
    return render(request, 'home/terms_conditions.html', {})

@gzip_page
def privacy(request):
    return render(request, 'home/privacy_policy.html', {})
