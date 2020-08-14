from django.db import models

class Address(models.Model):
	province = models.CharField(max_length = 40)
	district = models.CharField(max_length = 40)
	sector = models.CharField(max_length = 40)
	cell = models.CharField(max_length = 40)
	village = models.CharField(max_length = 40)