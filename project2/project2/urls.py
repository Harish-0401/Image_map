"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from imgapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.img_view),
    path('bodi/',views.bodi,name='bodi'),
    path('vira/',views.vira,name='virapandi'),
    path('boothi/',views.boothi,name='boothi'),
    path('meena/',views.meena,name='meena')
]
