# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from FabaniApp.models import Skill, Project, Comment

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Comment)
