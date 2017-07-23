from django.db import models

# Create your models here.
class Forecast(models.Model):
	date = models.DateField('Forecast date',unique=True)
	min_temp = models.IntegerField('Min temp')
	max_temp = models.IntegerField('Max temp')
	wind = models.IntegerField('Wind')
	rain = models.IntegerField('Rain')

	def __str__(self):
		return self.date.strftime("%Y-%m-%d")