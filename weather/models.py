from django.db import models
from django.urls import reverse

# Create your models here.


class City(models.Model):
    api_id = models.IntegerField()
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=3)
    lon = models.FloatField()
    lat = models.FloatField()
    coord = [lon, lat]
    def get_absolute_url(self):
        return reverse("weather-city_detail", kwargs={"pk": self.pk})
    
