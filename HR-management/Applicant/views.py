from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import RegistrationModel,ApplicationModel

class Logingapplicant(View):
    def get(self,request):
        return render(request,"applicantlogin.html")
    def post(self,request):
        us = request.POST.get('user')
        ps = request.POST.get('pas')
        if us == 'applicant' and ps == 'applicant':
            try:
                messages.success(request,"REGISTRATION")
                return render(request, "applicantlogin.html")
            except RegistrationModel.DoesNotExist:
                return redirect('applicant')
        else:
            try:
                RegistrationModel.objects.get(username=us,password=ps)
                return render(request,"applicantionform.html")
            except RegistrationModel.DoesNotExist:
                return redirect('applicant')
def registationform(request):

    return render(request,"applicantregister.html")


def register_details(request):
    na=request.POST.get("name")
    dt=request.POST.get("dat")
    email=request.POST.get("em")
    gn=request.POST.get("gen")
    mb=request.POST.get("mob")
    addr=request.POST.get("add")
    user=request.POST.get("us")
    pas=request.POST.get("pas")
    RegistrationModel(name=na,dob=dt,email=email,gender=gn,mobileno=mb,address=addr,username=user,password=pas).save()
    messages.success(request,"save to the details")
    return redirect('registration')


def applicationdetails(request):
    nam=request.POST.get("na")
    dat=request.POST.get("da")
    ema=request.POST.get("email")
    gend=request.POST.get("gen")
    mobi=request.POST.get("mobile")
    adde=request.POST.get("address")
    qual=request.POST.get("quali")
    po=request.POST.get("post")
    pe=request.POST.get("per")
    fi=request.POST.get("file")
    ApplicationModel(nam=nam,date=dat,emaii=ema,gend=gend,mobil=mobi,addres=adde,qualificatio=qual,post=po,perce=pe,file=fi).save()

    return render(request,"applicantionform.html")