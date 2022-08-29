from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .serializers import PatientSerializer
from .models import Patient
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


# def get_tokens_for_Patient(Patient):
#     refresh = RefreshToken.for_Patient(Patient)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, Patient):
#         token = super().get_token(Patient)

#         # Add custom claims
#         token['email'] = Patient.email
#         token['role'] = Patient.role
#         # ...

#         return {email:email,token:token}


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterView(APIView):
class RegisterView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient=serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(patient)  
        tokena = AccessToken().for_user(patient)
        tokena['email'] = patient.email
        tokena['role'] = patient.role
        response = Response()
        response.data = {
            'Patient':serializer.data,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response




class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        patient = Patient.objects.filter(email=email).first()
        if patient is None:
            raise AuthenticationFailed('Patient not found!')

        if not patient.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        tokenr = TokenObtainPairSerializer().get_token(patient)  
        tokena = AccessToken().for_user(patient)
        tokena['email'] = patient.email
        tokena['role'] = patient.role
        response = Response()
        print("this is the response",response.data)
        response.set_cookie(key='jwt', value=tokena, httponly=True)
        response.data = {
            'id':patient.id,
            'email':patient.email,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response


class getPatient(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient,many=True)
        return Response(serializer.data)

class getPatientById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        patient = Patient.objects.get(id=id)
        serializer=PatientSerializer(patient,many=False)
        return Response(serializer.data)

class updatePatient(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        patient = Patient.objects.get(id=id)
        serializer=PatientSerializer(instance=patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deletePatient(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        patient = Patient.objects.get(id=id)
        patient.delete()
        return Response("Item Successfully Deleted")

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ValidateToken(APIView):
    def get(self, request):
        try:
            print("asdasdsadsadasdasd")
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            data=jwt.decode(token, "secret", algorithms=["HS256"])
            return Response(data)
        except Exception as e:
            return Response(e)
        
