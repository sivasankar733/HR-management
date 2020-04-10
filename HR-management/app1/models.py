from django.db import models


class AdminModel(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=8)
