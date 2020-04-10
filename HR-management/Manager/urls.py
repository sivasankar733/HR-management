"""projectmain_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView

from Manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('managerlog/',views.showindex.as_view(),name='managerlog'),
    path('recuirtment/',TemplateView.as_view(template_name="recuirtment.html"),name='recuirtment'),
    path('recuirtmentdetails/',views.redetails.as_view(),name='recuirtmentdetails'),
    path('modify/',views.modifyingdata.as_view(),name='modify'),

    path('updated/<int:pk>',views.updated.as_view(),name='updated'),
    path('redelete/',views.deletedata.as_view(),name='redelete'),
    path('redeletedata/<int:pk>',views.deleted.as_view(),name='redeletedata'),
    path('interviewsched/',views.interviewshedule,name='interviewsched'),
    path('interviewdetails/',views.interviewdetails,name='interviewdetails'),
    path('addto/',views.addingdetails,name='addto')





]
