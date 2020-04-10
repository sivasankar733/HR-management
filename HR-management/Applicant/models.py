from django.db import models

class RegistrationModel(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    gender=models.CharField(max_length=15)
    mobileno=models.IntegerField(unique=True)
    address=models.CharField(max_length=200)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)

class ApplicationModel(models.Model):
    nam=models.CharField(max_length=30)
    date=models.DateField()
    emaii=models.EmailField()
    gend=models.CharField(max_length=15)
    mobil=models.IntegerField(unique=True)
    addres=models.CharField(max_length=100)
    qualificatio=models.CharField(max_length=30)
    post=models.CharField(max_length=40)
    perce=models.IntegerField()
    file=models.FileField(upload_to="files_images/")

