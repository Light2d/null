from django.urls import path
from .views import organizator

urlpatterns = [
    path('organizator', organizator, name='organizator') 
]
