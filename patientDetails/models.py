from django.db import models
from patient.models import Patient


class PatientDetail(models.Model):
    id=models.AutoField(primary_key=True)
    contact= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    additionalInfo= models.CharField(max_length=255)
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
    )
