
from django.contrib import admin
from django.urls import path,include
from . import viwes
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', viwes.about),
    path('', viwes.home),
    path('articles/', include('articles.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
