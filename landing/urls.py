# landing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.soon, name='soon'),
    path('success/', views.success, name='success'),  # new success page
]
