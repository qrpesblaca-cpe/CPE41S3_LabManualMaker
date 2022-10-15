from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.downloadTemp, name='downloadTemp')
]