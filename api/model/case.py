from django.db import models


class Case(models.Model):
    user = models.ForeignKey("Patient", on_delete=models.CASCADE)
    background = models.TextField(default="")
    clinical_findings = models.TextField(default="")
    diagnostic_process = models.TextField(default="")
    intervention_and_treatment = models.TextField(default="")
    outcome = models.TextField(default="")
    discuss = models.TextField(default="")
    pathology = models.TextField(default="")
