from rest_framework import serializers
from .models import PatientDetail
from patient.serializers import PatientSerializer
from patient.models import Patient


class CreatePatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetail
        fields = '__all__'

class ListPatientDetailSerializer(serializers.ModelSerializer):
    
    patient = PatientSerializer(read_only=True)
    class Meta:
        model = PatientDetail
        fields = '__all__'


