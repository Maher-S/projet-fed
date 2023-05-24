

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    location = models.CharField(max_length=255)
    timestamped = models.CharField(max_length=255)
    date_scraped = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    
