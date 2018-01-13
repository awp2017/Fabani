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

import json

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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
                return redirect('home')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)

def register_view(request):
	if request.method == "GET":
		form = EmployerRegisterForm()
	elif request.method == "POST":
		form = EmployerRegisterForm(request.POST)
		#if form.is_valid():
			#user.Create....

class UserProfileView(DetailView):
    template_name = 'userProfile.html'
    model = User
    context_object_name = 'user'

class Projects(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'

class ProjectView(DetailView):
	template_name = 'project.html'
	model = Project;
	context_object_name = 'project'


class ContactView(View):
    template_name = 'contact.html'

class AboutView(View):
    template_name = 'about.html'

class ProjectCreateView(CreateView):
    template_name = 'createProject.html'
    form_class = forms.CreateProjectForm
    model = Project
    def get_success_url(self,*args,**kwargs):
        return reverse('project',kwargs = {'pk': self.object.pk } )
    def form_valid(self,form):
        project = form.save(commit=False)
        project.employer = self.request.user
        return super(ProjectCreateView,self).form_valid(form)

class UserProjects(ListView):
	template_name = 'UserProjects.html'
	model = Project
	context_object_name = 'projects'

class AddEditSkills(CreateView):
    model = Project
    form_class = forms.AddEditSkillForm
    template_name = 'createEditSkillList.html'
    context_object_name = 'addEditSkills'



