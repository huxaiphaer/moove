
from django.urls import path

from . import views

urlpatterns = [
    path('reports/', views.ReportView.as_view(), name='post-report'),
]
