from django.db import models


class Patient(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    sexual = models.CharField(max_length=10)
    is_valid = models.BooleanField(default=True)
