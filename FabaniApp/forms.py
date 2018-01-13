from django import forms
#from FabaniApp.models import Employer
from FabaniApp.models import Project, Skill, Comment
#class EmployerRegisterForm(forms.ModelForm):
#    class Meta:
#        model = Employer
#        fields = ('username','firstname','lastname','email')

class CreateProjectForm(forms.ModelForm):
    skills = forms.ModelChoiceField(queryset=Skill.objects.all())
    deadline = forms.DateTimeField(input_formats=["%m/%d/%Y %I:%M %p"])
    #deadline = forms.DateTimeField(widget = forms.widgets.DateTimeInput(format = ("%m %d %Y %H:%M")))
    class Meta:
        model = Project
        fields = ('title','description','deadline','payment','skills')
    def clean_skills(self):
        return [skill for skill in Skill.objects.filter(id__in=dict(self.data)["skills"])]

        #import pdb;pdb.set_trace()

#class EmployerRegisterForm(forms.ModelForm):
#    class Meta:
#        model = Employer
#        fields = ('username','first_name','last_name','email')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddEditSkillForm(forms.ModelForm):
    skills = forms.ModelChoiceField(queryset=Skill.objects.all())
    class Meta:
        model = Project
        fields = ("skills",)

    def clean_skills(self):
        return [skill for skill in Skill.objects.filter(id__in=dict(self.data)["skills"])]
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

