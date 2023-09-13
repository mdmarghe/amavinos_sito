from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.http import HttpResponse
from .models import * 

def catas_list(request):
    catas=Cata.objects.all().order_by('date')
    context={'catas':catas}
    return render(request,"catas/catas_list.html",context)

def cata_details(request,slug):
    return HttpResponse(slug)

