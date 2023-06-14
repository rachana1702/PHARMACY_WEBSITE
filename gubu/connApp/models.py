from django.db import models

# Create your models here.
class MyPharmacy(models.Model):
    #id : int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    visible = models.BooleanField(default=False)