from django import forms
#from FabaniApp.models import Employer
from FabaniApp.models import Project
#class EmployerRegisterForm(forms.ModelForm):
#    class Meta:
#        model = Employer
#        fields = ('username','firstname','lastname','email')

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','deadline','payment','skills')