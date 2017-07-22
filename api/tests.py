from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Create your tests here.
from .models import Forecast

class ForecastModelTests(TestCase):
	"""This class defines the test suite for the Forecast model."""
	
	def setUp(self):
		"""
		Define the test client and other test variables.
		"""
		self.forecast_date = timezone.now()
		self.forecast_min = 0
		self.forecast_max = 24
		self.forecast_wind = 10
		self.forecast_rain = 5
		self.forecast = Forecast(date=self.forecast_date,
								 min_temp=self.forecast_min,
								 max_temp=self.forecast_max,
								 wind=self.forecast_wind,
								 rain=self.forecast_rain
								 )

	def test_string_method(self):
		"""
		make sure that the correct date format is printed
		"""
		t = timezone.now()
		f = Forecast(date=t)
		self.assertEqual(f.__str__(),t.strftime("%Y-%m-%d")) 

	def test_model_can_create_a_forecast(self):
		"""
		Test the bucketlist model can create a bucketlist.
		"""
		old_count = Forecast.objects.count()
		self.forecast.save()
		new_count = Forecast.objects.count()
		self.assertNotEqual(old_count, new_count)
