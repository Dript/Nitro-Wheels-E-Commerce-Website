from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
	
	url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    	url(r'^admin/', admin.site.urls),
    	url(r'^nitro_wheels/',include('nitro_wheels.urls')),
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
