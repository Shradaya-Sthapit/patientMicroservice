from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum

#Create your models here.

# class Roles(Enum):
#     PATIENT="PATIENT"
#     DOCTOR="DOCTOR"
#     ADMIN="ADMIN"

#     @classmethod
#     def choices(cls):
#         return tuple((i.name, i.value) for i in cls)

class Patient(AbstractUser):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255,unique=True)
    password= models.CharField(max_length=255)
    username=None
    role=models.CharField(max_length=255,default='PATIENT')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
