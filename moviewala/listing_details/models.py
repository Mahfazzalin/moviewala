from django.db import models


# Create your models here.
class movie_details(models.Model):
    name = models.CharField(max_length=200)
    cover_link = models.URLField(max_length=500)
    language = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=30)
    textbox = models.TextField()
    d_link = models.URLField(max_length=500)
    ss_1 = models.URLField(max_length=500)
    ss_2 = models.URLField(max_length=500)
    ss_3 = models.URLField(max_length=500)
    ss_4 = models.URLField(max_length=500)
