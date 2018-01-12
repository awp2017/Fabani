# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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