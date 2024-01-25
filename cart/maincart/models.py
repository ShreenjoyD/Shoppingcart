from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.
class details(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics/')
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('maincart:purchase', args=[self.id])
