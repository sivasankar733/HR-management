from django import forms
from .models import AdminModel
from Admin.models import AddemployeeModel

class AdminForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AdminModel
        fields="__all__"

class AddemployeeForm(forms.ModelForm):
    edesignation=(
        ('developer','developer'),
        ('manager','manager'),
        ('teamleader','tl')
    )
    edesignation=forms.ChoiceField(choices=edesignation)
    eidno=forms.IntegerField(min_value=1001)
    class Meta:
        model=AddemployeeModel
        fields='__all__'

    def clean_esalary(self):
        esal=self.cleaned_data["esalary"]
        if esal>=10000:
            return esal
        else:
            raise forms.ValidationError('salary must be min 10000')