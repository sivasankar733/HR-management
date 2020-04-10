from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from Admin.forms import AdminForm,AddemployeeForm
from Admin.models import AdminModel,AddemployeeModel

class loging(View):
    def get(self,request):
        return render(request,"adminlog.html",{"af":AdminForm()})
    def post(self,request):
        uname=request.POST['username']
        pas=request.POST['password']
        if uname=="admin@gmail.com" and pas=="admin":

            return render(request,"loging_details.html")
        else:
            messages.success(request,"inavlid email and password ")
            return redirect('adminlog')

class addemploye(View):

    def get(self,request):
        addm = AddemployeeModel()
        return render(request,"addemp.html",{"adf":AddemployeeForm(),"adm":addm})
    def post(self,request):
        addf=AddemployeeForm(request.POST)
        if addf.is_valid():
            addf.save()
            messages.success(request,"Emp details was saved")
            return redirect("addemp")
        else:
            addm= AddemployeeModel(request.POST)
            return render(request,"addemp.html",{"adf":addf,"adm":addm},)
class viewemploye(ListView):
    model=AddemployeeModel
    template_name = "viewemp.html"
    fields='__all__'
class updateemp(ListView):
    model=AddemployeeModel
    template_name = "update.html"

class modifyemployee(UpdateView):
    model = AddemployeeModel
    template_name = "modify.html"
    fields = "__all__"
    success_url = "/update_emp/"
class delete_employee(ListView):
    model=AddemployeeModel
    template_name = "delete.html"

class delete(DeleteView):
    model = AddemployeeModel
    template_name = "deleteemp.html"
    fields = "__all__"
    success_url = "/update_emp/"

