"""AjaxExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from Application import views

urlpatterns = [
<<<<<<< HEAD
	url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
	path('admin/', admin.site.urls),
	path('', views.index, name = 'index'),
	path('saveData/', views.saveData, name = 'saveData'),
	path('delete/', views.delete, name = 'delete'),
	path('edit/', views.edit, name = 'edit'),
	path('demo/', views.demo, name = 'demo'),
=======
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('', views.index, name = 'index'),
    path('saveData/', views.saveData, name = 'saveData'),
    path('delete/', views.delete, name = 'delete'),
    path('edit/', views.edit, name = 'edit'),
    path('demo/', views.demo, name = 'demo'),
>>>>>>> 7d1ad9c9012e69feccf35483bddb7c9bd3f9cd44
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
