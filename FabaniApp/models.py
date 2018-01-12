# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Skill(models.Model):
	name = models.CharField(max_length = 30, blank = False)
	description = models.CharField(max_length = 200, blank = True)
	proficiency = models.PositiveSmallIntegerField(choices=[
            (1, "Beginner"),
            (2, "Junior"),
            (3, "Middle"),
            (4, "Senior"),
            (5, "Expert"),
        ], default = 1)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Project(models.Model):
    title = models.CharField(max_length=45)
    # idEmployee = models.ManyToManyField(Employee, null=True)
    # idEmployer = models.ForeignKey(Employer)
    skills = models.ManyToManyField(Skill, related_name='project_skills')
    deadline = models.DateField()
    payment = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    applications = models.ManyToManyField(Project, related_name='employee_applications')
    projectInProgress = models.ManyToManyField(Project, related_name='employee_projectInProgress')

@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.profile.save()



