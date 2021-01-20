from django.shortcuts import render, HttpResponse,redirect
from. import models
from django.contrib.auth.decorators import login_required
from. import forms

def articles_list(request):
    articles=models.Article.objects.all().order_by('-date')
    return render(request,'articles/articleslist.html',{'articles':articles})

def article_explain(request,slug):
    # return HttpResponse (slug)
    article=models.Article.objects.get(slug=slug)
    return render(request,'articles/articles_detail.html',{'article':article})

@login_required(login_url="/accunts/login")
def articles_create(request):
    if request.method =="POST":
        form=forms.CreaterArticle(request.POST,request.FILES)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form=forms.CreaterArticle()
    return render(request,'articles/articles_create.html',{'form':form})
