from django.db import models

class interviewModel(models.Model):
    interviewid=models.IntegerField(primary_key=True)
    interviewer=models.IntegerField(unique=True)
    scheduledate=models.DateField()
    applicantid=models.IntegerField(unique=True)
    result=models.CharField(max_length=40)
