from django.urls import path
from . import views

urlpatterns = [
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
]
