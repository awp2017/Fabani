# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from FabaniApp.models import Project,Comment, Skill
from FabaniApp import forms
from FabaniApp.forms import CreateProjectForm, LoginForm

import json

def login_view(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('projects_list')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')

def register_view(request):
	if request.method == "GET":
		form = EmployerRegisterForm()
	elif request.method == "POST":
		form = EmployerRegisterForm(request.POST)
		#if form.is_valid():
			#user.Create....

class UserProfileView(TemplateView):
    template_name = 'userProfile.html'
    model = User
    context_object_name = 'user'

class ProjectsView(ListView):
    template_name = 'home.html'
    model = Project
    context_object_name = 'projects'

class ProjectView(DetailView):
	template_name = 'project.html'
	model = Project;
	context_object_name = 'project'


class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ProjectCreateView(CreateView):
    template_name = 'createProject.html'
    form_class = CreateProjectForm
    model = Project
    def get_success_url(self,*args,**kwargs):
        return reverse('project',kwargs = {'pk': self.object.pk } )
    def form_valid(self,form):
        project = form.save(commit=False)
        project.employer = self.request.user
        return super(ProjectCreateView,self).form_valid(form)

class UserProjects(ListView):
	template_name = 'userProjects.html'
	model = Project
	context_object_name = 'projects'

class AddEditSkills(CreateView):
    model = Project
    form_class = forms.AddEditSkillForm
    template_name = 'createEditSkillList.html'
    context_object_name = 'addEditSkills'



