from django.db import models

# Create your models here.
class ContactUsInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    msg = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + ' : ' + self.email
