# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

import json

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register_view(request):
	if request.method == "GET":
		form = EmployerRegisterForm()
	elif request.method == "POST":
		form = EmployerRegisterForm(request.POST)
		#if form.is_valid():
			#user.Create....


class employerProfile(DetailView):
    template_name = 'employerProfile.html'
   # model = Employer
    # context_object_name = 'employer'