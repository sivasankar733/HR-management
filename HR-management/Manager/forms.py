from django import forms
from Manager.models import ManagerModel
from .models import RecuirtmentModel
class ManagerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=ManagerModel
        fields='__all__'

class  RecuirtmentForm(forms.ModelForm):
    regi_form=forms.DateField(help_text="yyy-mm-dd")
    lastdob=forms.DateField(help_text="yyy-mm-dd")
    class Meta:
        model=RecuirtmentModel
        fields='__all__'