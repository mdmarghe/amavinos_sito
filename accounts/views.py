from django.shortcuts import render
from django.http import HttpResponse


def signup_view(request):
    #articles=Article.objects.all().order_by('date')
   # context={'articles':articles}
    #return render(request,"articles/article_list.html",context)
    return render(request, 'accounts/signup.html')