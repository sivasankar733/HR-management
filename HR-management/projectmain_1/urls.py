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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
import Admin.urls as Admin
import Manager.urls as Manager
import Applicant.urls as Applicant
import Interviewer.urls as Interviewer
import HRhead.urls as HRhead
from projectmain_1 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Admin)),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('',include(Manager)),
    path('',include(Applicant)),
    path('',include(Interviewer)),
    path('',include(HRhead)),

]
