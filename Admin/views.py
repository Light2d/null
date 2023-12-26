from django.shortcuts import render
from Auth.models import CustomUser
from App.models import Direction, Event

def organizator(request):

    return render(request, 'organizator.html')
