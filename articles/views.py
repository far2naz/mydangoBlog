from django.shortcuts import render
from. import models

def articles_list(request):
    articles=models.Article.objects.all()
    return render(request,'articles/articleslist.html',{'articles':articles})
