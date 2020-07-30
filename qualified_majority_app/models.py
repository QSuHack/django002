from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    territory = models.IntegerField()