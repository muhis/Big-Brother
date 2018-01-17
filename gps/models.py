from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Coordinate(models.Model):
    """
    One coordinate reported
    """
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
