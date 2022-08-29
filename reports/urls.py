
from django.urls import path

from . import views

urlpatterns = [
    path('vehicles/', views.VehicleView.as_view(), name='vehicles'),
    path('trips/', views.TripView.as_view(), name='trips'),
    path('exceptions/', views.ExceptionsView.as_view(), name='exceptions'),
    path('reports/', views.ReportView.as_view(), name='post-report'),
]
