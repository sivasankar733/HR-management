from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, ListView, DeleteView
from Manager.forms import ManagerForm, RecuirtmentForm
from Manager.models import RecuirtmentModel, InterviewsheduleModel


class showindex(View):
    def get(self, request):
        return render(request, "managerlog.html", {"mf": ManagerForm()})

    def post(self, request):
        uname = request.POST["username"]
        pas = request.POST["password"]
        if uname == 'manager@gmail.com' and pas == "manager":
            return render(request, "managerhome.html")
        else:
            messages.success(request, "invalid username and password")
            return render(request, "managerlog.html")


class redetails(View):
    def get(self, request):
        rem=RecuirtmentModel()
        mess = messages.success(request, "updated detais")

        return render(request, "redetails.html", {"rf": RecuirtmentForm(),"rm":rem})

    def post(self, request):
        ref = RecuirtmentForm(request.POST)
        if ref.is_valid():
            ref.save()

            messages.success(request, "details was added")
            return redirect("recuirtmentdetails")
        else:
            messages.success(request, "invalid recuirtment details")
            return redirect("recuirtmentdetails")

class modifyingdata(View):
    def post(self,request):
        i=request.POST.get("t1")

        try:
            rem=RecuirtmentModel.objects.filter(oppcode=i).get(oppcode=i)
            print(rem)

            return render(request,"codegetdetails.html",{"rm":rem})
        except RecuirtmentModel.DoesNotExist:

            messages.success(request,"invalid code")
            return redirect('modify')

    def get(self,request):

        return render(request,"recuirt_modify.html")

class updated(UpdateView):
    model=RecuirtmentModel
    template_name = "codegetdetails.html"
    fields = "__all__"
    success_url = "/modify/"
class deletedata(ListView):
    model = RecuirtmentModel
    template_name = "redelete.html"
class deleted(DeleteView):
    model = RecuirtmentModel
    template_name = "redeleted.html"
    fields='__all__'
    success_url = "/redelete/"


def interviewshedule(request):
    return render(request,"interviewsch.html")

def interviewdetails(request):
    inter=request.POST.get("a1")
    iv=InterviewsheduleModel(applicantid=inter)
    return render(request,"interviewapplicant.html",{"ivm":iv})


def addingdetails(request):
    ap=request.POST.get("appid")
    em=request.POST.get("emp")
    dt=request.POST.get("date")
    im=InterviewsheduleModel(sheduedate=dt,selectempid=em,applicantid=ap).save()
    messages.success(request,"adding details")
    return render(request,"interviewapplicant.html")