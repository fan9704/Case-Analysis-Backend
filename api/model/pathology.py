from django.db import models


class Pathology(models.Model):
    user = models.ForeignKey("Patient", on_delete=models.CASCADE)
    specimen_source = models.TextField()
    specimen_type = models.TextField()
    specimen_size = models.TextField()
    check_description = models.TextField()
    summary = models.TextField()
    addition_test = models.TextField()
