from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles=Article.objects.all().order_by('date')
    context={'articles':articles}
    return render(request,"articles/article_list.html",context)

def article_details(request,slug):
    #return HttpResponse(slug)
    article=Article.objects.all().get(slug=slug)
    context={'article':article}
    return render(request, 'articles/article_detail.html', context)


@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')