from django.db import models

# Create your models here.

class User(models.Model):
	email = models.EmailField('Registration email address', max_length=254)
	password = models.CharField('Registration password', max_length=256)
	# password_repeat = models.CharField('Registration password repeat', max_length=256)

	def __str__(self):
			return self.email

# class LoginForm(models.Model):
# 	email = models.EmailField('Login email address', max_length=254)
# 	password = models.CharField('Login password', max_length=256)

# 	def __str__(self):
# 		return self.email

class Weather(models.Model):
	date = models.DateField('Weather date')
	min_temp = models.IntegerField('Weather min temp')
	max_temp = models.IntegerField('Weather max temp')
	wind = models.IntegerField('Weather wind')
	rain = models.IntegerField('Weather rain')

	def __str__(self):
		return self.date.strftime("%Y-%m-%d")
