from django.contrib import messages
from django.shortcuts import render, redirect

from Interviewer.models import interviewModel


def interviewerlog(request):
    us=request.POST.get("user")
    ps=request.POST.get("pas")
    if us=="siva" and ps=="siva":
        return render(request,"fselectionlist.html")
    else:
        messages.success(request,"invalid username and password")
        return redirect("interviewer")

def inter_applicantid(request):
    appid=request.POST.get("id")
    im=interviewModel(applicantid=appid)
    return render(request,"interapplicantid.html",{"ivm":im})


def intervieweshedule(request):
    ini=request.POST.get("inid")
    inte=request.POST.get("inter")
    da=request.POST.get("dat")
    ap=request.POST.get("appl")
    re=request.POST.get("res")
    interviewModel(interviewid=ini,interviewer=inte,scheduledate=da,applicantid=ap,result=re).save()
    messages.success(request,"details was saved")
    return redirect("interapplicantid")