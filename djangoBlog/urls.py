
from django.contrib import admin
from django.urls import path,include
from . import viwes
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from articles.views import articles_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', viwes.about),
    path('articles/', include('articles.urls')),
    path('accunts/', include('accunts.urls')),
    path('',articles_list),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
