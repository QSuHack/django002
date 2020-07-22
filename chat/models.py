from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#
class Group(models.Model):
    name = models.CharField(max_length=50)
    creation_date=models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(to=User)
class Message(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sending_user")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient_user", null=True, blank =True
    )
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)


