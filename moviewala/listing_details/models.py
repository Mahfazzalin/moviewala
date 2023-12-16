from django.db import models


# Create your models here.
class movie_details(models.Model):
    name = models.CharField(max_length=200)
    cover_link = models.URLField(max_length=500)
    language = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=30)
    description = models.TextField()
    drive_link = models.URLField(max_length=500)
    screenshot_1 = models.URLField(max_length=500)
    screenshot_2 = models.URLField(max_length=500)
    screenshot_3 = models.URLField(max_length=500)
    screenshot_4 = models.URLField(max_length=500)
