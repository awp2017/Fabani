from django import forms
from app.models import Employer 
class EmployerRegisterForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('username','firstname','lastname','email')