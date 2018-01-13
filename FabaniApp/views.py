# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from FabaniApp.models import Project

from FabaniApp.models import Project, Comment

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

class UserProjects(ListView):
	template_name = 'UserProjects.html'
	model = Project
	context_object_name = 'projects'
