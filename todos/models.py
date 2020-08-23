from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    class Status(models.IntegerChoices):
        TODO = 0
        DOING =1
        DONE= 2
        ARCHIVED=3
    task_status = models.IntegerField(choices=Status.choices, default=0)
    title = models.CharField(max_length=50)
    details = models.TextField()
    assigned = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    expiry_time = models.DateTimeField(verbose_name="Expiry time")
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)