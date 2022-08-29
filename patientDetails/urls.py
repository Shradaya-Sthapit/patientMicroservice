from django.urls import path,include
from .views import createPatientDetail,getPatientDetail,getPatientDetailById,deletePatientDetail,updatePatientDetail


urlpatterns = [

    path('create',  createPatientDetail.as_view()),
    path('get', getPatientDetail.as_view()),
    path('get/<str:id>', getPatientDetailById.as_view()),
    path('update/<str:id>', updatePatientDetail.as_view()),
    path('delete/<str:id>', deletePatientDetail.as_view()),
]

