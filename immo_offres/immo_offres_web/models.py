from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    price = models.IntegerField()  # Change from DecimalField to IntegerField
    location = models.CharField(max_length=255)
    timestamped = models.CharField(max_length=255)
    date_scraped = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    images = models.TextField(max_length=255)  # Add new column for image URLs
