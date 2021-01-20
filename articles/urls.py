from django.urls import path
from . import views

app_name="articles"
urlpatterns = [

    path('', views.articles_list,name="list"),
    path('create', views.articles_create,name="create"),
    path('<slug>',views.article_explain,name="explain")

]
