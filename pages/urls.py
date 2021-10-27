from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.faq, name='faq'),
    path('return-policy/', views.return_policy, name='return_policy'),
]
