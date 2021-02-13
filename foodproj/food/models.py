from django.db import models

class Food(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=2000)