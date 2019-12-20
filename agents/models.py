from django.db import models

# Create your models here.
class agents(models.Model):
    type = models.CharField(max_length=30)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    agent_image = models.ImageField(upload_to='agent_image')
    phone = models.CharField(max_length=30)
    state_license_id = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fname
