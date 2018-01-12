# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_employer_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
    skills = models.ManyToManyField(Skill, null=True)
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




