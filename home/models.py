from django.db import models
from agents.models import agents

# Create your models here.
class property(models.Model):
    status_choice = (
        ('Coming Soon', 'Coming Soon'),
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    )
    agent = models.ForeignKey(agents, on_delete=models.CASCADE)
    heading = models.CharField(max_length=250)
    location = models.CharField(max_length=500)
    zip = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    price = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    area = models.IntegerField()
    build_yr = models.IntegerField()
    notes = models.TextField()
    tax_applicable = models.BooleanField(default=False)
    estimated_payment = models.IntegerField()
    vr_url = models.CharField(max_length=500)
    aerial_video_url = models.CharField(max_length=500)
    display_img = models.ImageField(upload_to='display_image')
    satellite_img = models.ImageField(upload_to='satellite_image')
    google_map_url = models.CharField(max_length=500)
    listing_owner = models.CharField(max_length=500)
    listing_agent = models.CharField(max_length=500)
    status = models.CharField(max_length=12, choices=status_choice)
    is_featured = models.BooleanField(default=False)
    brochure = models.FileField(upload_to='brochure')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.heading, self.created)

class images(models.Model):
    property = models.ForeignKey(property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_image')