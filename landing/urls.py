from django.urls import path
from .views import soon

urlpatterns = [
    path('', soon, name='soon'),
]
