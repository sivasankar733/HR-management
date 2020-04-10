from django.contrib import messages
from django.shortcuts import render, redirect
from Applicant.models import ApplicationModel
from Interviewer.models import interviewModel



def hrheadhome(request): 
    us=request.POST.get("user")
    ps=request.POST.get("pas")
    if us=="hrhead" and ps=="hrhead":
        return render(request,"hrheadmain.html")
    else:
        messages.success(request,"invalid username and password")
        return redirect("hrhead")


def shortlist_details(request):
    am=ApplicationModel.objects.all()
    return render(request,"shortlist.html",{"apm":am})


def selected_details(request):

    im=interviewModel.objects.filter(result='select')
    return render(request,"select.html",{"im":im})


def rejected_details(request):
    rm=interviewModel.objects.filter(result='reject')
    return render(request,"reject.html",{"rm":rm})