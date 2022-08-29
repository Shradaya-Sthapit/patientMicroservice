from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreatePatientDetailSerializer,ListPatientDetailSerializer
from .models import PatientDetail
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createPatientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        patient= request.user
        request.data['patient']=patient.id
        serializer = CreatePatientDetailSerializer(data=request.data)
        serializer.patient=patient
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getPatientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patientDetail = PatientDetail.objects.all()
        serializer=ListPatientDetailSerializer(patientDetail,many=True)
        return Response(serializer.data)

class getPatientDetailById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        patientDetail = PatientDetail.objects.get(id=id)
        serializer=ListPatientDetailSerializer(patientDetail,many=False)
        return Response(serializer.data)

class updatePatientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        print("la la la ra la la")
        patientDetail = PatientDetail.objects.get(id=id)
        
        serializer=CreatePatientDetailSerializer(instance=PatientDetail,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deletePatientDetail(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        patientDetail = PatientDetail.objects.get(id=id)
        patientDetail.delete()
        return Response("Item Successfully Deleted")



    