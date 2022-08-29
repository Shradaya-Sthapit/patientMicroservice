from django.urls import include, path
from . import views
from .views import  getDoctorById,getDoctor
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  
    path('get', getDoctor.as_view()),
    path('get/<str:id>', getDoctorById.as_view()),

]

