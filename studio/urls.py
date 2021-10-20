from django.urls import path
from . import views

urlpatterns = [
    path('studio/', views.studio, name='studio'),
]