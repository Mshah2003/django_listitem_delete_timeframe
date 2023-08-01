from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from datetime import timedelta


# Create your views here.

def home(request):
    ls = Date.objects.all()
    thirty_days_ago = timezone.now() - timedelta(days=30)
    old_objects = Date.objects.filter(date__lt = thirty_days_ago)
    old_objects.delete()

    return render(request , 'home.html',locals())

def details(request,pk):
    abc = get_object_or_404(Date,id = pk)
    return render(request,"details.html",locals())