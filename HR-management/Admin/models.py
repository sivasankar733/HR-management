from django.db import models


class AdminModel(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=8)


class AddemployeeModel(models.Model):
    eidno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    esalary=models.FloatField()
    edesignation=models.CharField(max_length=30)