# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from FabaniApp.models import Employee, Project, Skill

# Register your models here.

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Skill)