from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient-list'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('measure/<int:pk>/', views.MeasureDetailView.as_view(), name='measure-detail'),
    path('measure/<int:pk>/', views.MeasureListView.as_view(), name='measure-list'),
    path('measure/create/', views.MeasureCreateView.as_view(), name='measure-create'),
    path('measure/<int:pk>/update/', views.MeasureUpdateView.as_view(), name='measure-update'),
]
