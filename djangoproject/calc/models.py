from django.db import models

class Cur(models.Model):
	currency_name = models.CharField(max_length = 70)
	rate1 = models.FloatField(null = False, default = 1)
	rate2 = models.FloatField(null = False, default = 1)
	rate3 = models.FloatField(null = False, default = 1)
	rate4 = models.FloatField(null = False, default = 1)
	lastupdated = models.DateTimeField(blank = True)

	def __str__(self):
		return self.currency_name

class CompareOutput(models.Model):
	id = models.AutoField(primary_key=True)
	rate = models.FloatField()
	name = models.CharField(max_length = 50)
	link = models.URLField()

	def __str__(self):
		return self.name


# Create your models here.
