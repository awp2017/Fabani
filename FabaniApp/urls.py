"""Fabani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from FabaniApp import views

urlpatterns = [
    url(r'^$', views.ProjectsView.as_view(), name='projects_list'),
    url(r'^user_projects/(?P<pk>[0-9]+)/$', views.UserProjects.as_view(), name='user_projects'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
<<<<<<< HEAD
    url(r'^project/add/$',views.ProjectCreateView.as_view(), name='project_create'),
    # url(r'^employer/(?P<pk>[0-9]+)/$', views.EmployerProfileView.as_view(), name='employer_profile'),
=======
    url(r'^project/(?P<pk>[0-9]+)/addComment/$', views.AddCommentView.as_view(), name='comment'),
>>>>>>> Fuck that database
    #url(r'^employer/register/$', views.EmployerRegisterView.as_view(), name='employer_register'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),


]
