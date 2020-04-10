from django.db import models


class ManagerModel(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=30)

class RecuirtmentModel(models.Model):
    depart=(("DEVELOPER",'DEVELOPER'),
            ("TESTER","tester"),
            ("designer","DESIGNER"),
            ("MANAGER","manager"))
    oppcode=models.IntegerField(primary_key=True)
    qualification=models.CharField(max_length=30)
    regi_form=models.DateField(help_text="yyyy-mm-dd")
    age=models.IntegerField()
    lastdob=models.DateField(help_text="yyyy-mm-dd")
    department=models.CharField(choices=depart,max_length=40)
    positions=models.IntegerField()
    description=models.CharField(max_length=100)
    respon=models.CharField(max_length=50)
    contactno=models.IntegerField(unique=True)

class InterviewsheduleModel(models.Model):
    applicantid=models.IntegerField(primary_key=True)
    selectempid=models.IntegerField(unique=True)
    sheduedate=models.DateField(help_text="yyyy-mm-dd")
