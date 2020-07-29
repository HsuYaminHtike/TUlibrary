# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Elibrary(models.Model):
	
	student_name = models.CharField(max_length=255)
	student_rollNo = models.CharField(max_length=100)
	book_name = models.CharField(max_length=255)
	date = models.DateTimeField()
	feedback = models.CharField(max_length=255)
