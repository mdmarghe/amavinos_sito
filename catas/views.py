from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.decorators import login_required

def catas_list(request):
    catas=Cata.objects.all().order_by('date')
    context={'catas':catas}
    return render(request,"catas/catas_list.html",context)

def cata_details(request,slug):
    cata=Cata.objects.get(slug=slug)
    return HttpResponse(slug)


@login_required(login_url="/catas/login/")
def cata_create(request):
    return render(request, 'catas/cata_create.html')

