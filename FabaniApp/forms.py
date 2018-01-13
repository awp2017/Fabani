from django import forms
from app.models import Employer, Employee, Project
class EmployerRegisterForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('username','first_name','last_name','email')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ApplyToProject(forms.ModelForm):
    class Meta:
        model = Project
