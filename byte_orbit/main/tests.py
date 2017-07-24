from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from .utils import get_data, clean_json, load_forecasts
import datetime



# Create your tests here.
from .models import Forecast

class ForecastModelTests(TestCase):
	"""This class defines the test suite for the Forecast model."""	
	def setUp(self):
		"""
		Define the test client and other test variables.
		"""
		self.forecast_date = datetime.date.fromordinal(45)
		
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
		t = datetime.date.fromordinal(45)
		f = Forecast(date=t)
		self.assertEqual(f.__str__(),t.strftime("%Y-%m-%d")) 

	def test_model_can_create_a_forecast(self):
		"""
		Test the forecast model can create a forecast.
		"""
		old_count = Forecast.objects.count()
		self.forecast.save()
		new_count = Forecast.objects.count()
		self.assertNotEqual(old_count, new_count)

	

class ViewTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
		"""Define the test client and other test variables."""
		self.client = APIClient()
		user = User.objects.create(username='testuser')
		self.client.force_login(user=user)

		self.forecast_data = {'date': datetime.date.fromordinal(30),'min_temp':0,'max_temp':25,'wind':5,'rain':10}

		self.response = self.client.post(
			reverse('main:create'),
			self.forecast_data,
			format='json')

	def test_api_can_create_a_forecast(self):
		"""Test the api can CREATE a forecast."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_forecast(self):
		"""Test the api can GET a forecast."""
		forecast = Forecast.objects.get()
		response = self.client.get(
			reverse('main:details',kwargs={'pk': forecast.id})
			, format='json')

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, forecast)

	def test_api_can_update_a_forecast(self):
		"""Test the api can UPDATE a forecast."""
		forecast = Forecast.objects.order_by("date").first()
		forecast_update = {'date':forecast.date,'min_temp':0,'max_temp':25,'wind':5,'rain':10}
		response = self.client.put(
			reverse('main:details', kwargs={'pk': forecast.id}),
			forecast_update, format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_api_can_delete_a_forecast(self):
		"""Test the api can DELETE a forecast."""
		forecast = Forecast.objects.first()
		response = self.client.delete(
			reverse('main:details', kwargs={'pk': forecast.id}),
			format='json',
			follow=True)

		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_can_load_database(self):
		load_forecasts()
		forecast = Forecast.objects.get(date=timezone.now().date())
		self.assertEqual(forecast is not None,True)

class JSONTests(TestCase):
	"""
	Test that the 'dirty' JSON from weather24 has been sufficiently cleaned
	"""

	def test_can_clean_json(self):
		text = '{"Date":new Date(Date.UTC(2017,6,23,22,0,0,0))};/*'

		self.assertEqual(clean_json(text),'{"Date":"2017-07-24"}')

		# in: "Date":new Date(Date.UTC(2017,6,22,22,0,0,0))
		# out: "Date":"2017-07-23"

    






# Create your tests here.
class IndexViewTests(TestCase):
	"""
	Testing the results of the landing page
	"""
	def setUp(self):
		self.client = Client()
		user = User.objects.create(username='testuser')
		self.client.force_login(user=user)

	def test_not_logged_in(self):
		"""
		Arriving on the landing page while not authenticated
		"""
		badclient = Client()
		response = badclient.get(reverse('main:index'), follow=True)
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Please <a href="/register/">register an account</a> or <a href="/login/">log in.</a>')

	def test_logged_in(self):
		"""
		Arriving on the landing page while authenticated
		"""
		response = self.client.get(reverse('main:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Hi testuser!')


class ResultsViewTests(TestCase):
	"""
	Testing the responses of the results view
	"""
	
	def setUp(self):
		self.client = Client()
		user = User.objects.create(username='testuser')
		self.client.force_login(user=user)

	def test_not_logged_in(self):
		"""
		Arriving on the results page while not authenticated
		"""
		badclient = Client()
		response = badclient.get(reverse('main:results'), follow=True)
		self.assertEqual(response.redirect_chain[0], ('/login/?next=/weather/', 302))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Kindly fill in your details below.')

	def test_logged_in(self):
		"""
		Arriving on the results page while authenticated
		"""
		response = self.client.get(reverse('main:results'), follow=True)

		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Hi testuser!')

class LoginViewTests(TestCase):
	"""
	Testing the responses of the login view
	"""

	def setUp(self):
		self.client = Client()
		user = User.objects.create(username='testuser')
		self.client.force_login(user=user)

	def test_not_logged_in(self):
		"""
		Arriving on the login page while not authenticated
		"""
		badclient = Client()
		response = badclient.get(reverse('login'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Kindly fill in your details below.')

	def test_logged_in(self):
		"""
		Arriving on the login page while authenticated
		"""
		response = self.client.get(reverse('login'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, 'Kindly fill in your details below.')