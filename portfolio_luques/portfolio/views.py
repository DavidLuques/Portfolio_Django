from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Proyecto

def home(request):
    return render(request,'home.html')
