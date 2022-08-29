from django.urls import include, path
from . import views
from .views import RegisterView, LoginView, getPatientById,getPatient,updatePatient,deletePatient,LogoutView,ValidateToken
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register',  RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('get', getPatient.as_view()),
    path('get/<str:id>', getPatientById.as_view()),
    path('update/<str:id>', updatePatient.as_view()),
    path('delete/<str:id>', deletePatient.as_view()),
    path('logout', LogoutView.as_view()),
    path('validate', ValidateToken.as_view()),

]

