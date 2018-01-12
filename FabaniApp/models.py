# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=45)
    # idEmployee = models.ManyToManyField(Employee, null=True)
    # idEmployer = models.ForeignKey(Employer)
    # idSkillList = models.ForeignKey(SkillList)
    deadline = models.DateField()
    payment = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # idProject = models.ForeignKey(Project)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.textsssclass Skill(models.Model):
	name = models.CharField(max_length = 30, blanck = False)
	proficiency = models.PositiveSmallIntegerField(choices=[
            (1, "Beginner"),
            (2, "Junior"),
            (3, "Middle"),
            (4, "Senior"),
            (5, "Expert"),
        ], default = 1)

	def __str__(self):
        return self.name
        
class Skill(models.Model):
	name = models.CharField(max_length = 30, blanck = False)
	proficiency = models.PositiveSmallIntegerField(choices=[
            (1, "Beginner"),
            (2, "Junior"),
            (3, "Middle"),
            (4, "Senior"),
            (5, "Expert"),
        ], default = 1)

	def __str__(self):
        return self.name