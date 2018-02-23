from django.db import models

# Create your models here.

class StudyGroup(models.Model):
	venue = models.CharField(blank=False, max_length=1000)
	time = models.CharField(blank=False, max_length=1000)
	topic = models.CharField(blank=False, max_length=1000)
	date =  models.CharField(blank=False, max_length=1000)

	