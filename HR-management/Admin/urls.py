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
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from Admin import views
from projectmain_1 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlog/',views.loging.as_view(),name='adminlog'),
    path('addemp/',views.addemploye.as_view(),name='addemp'),
    path('view_employee/',views.viewemploye.as_view(),name='view_employee'),
    path('update_emp/',views.updateemp.as_view(),name='update_emp'),
    path('modifyemp/<int:pk>',views.modifyemployee.as_view(),name='modifyemp'),
    path('delete_emp/',views.delete_employee.as_view(),name='delete_emp'),
    path('deleteemp/<int:pk>',views.delete.as_view(),name='deleteemp')



]
