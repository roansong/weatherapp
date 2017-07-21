from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

# Create your tests here.
from .models import Forecast

class ForecastModelTests(TestCase):

	def test_string_method(self):
		"""
		make sure that the correct date format is printed
		"""
		t = timezone.now()
		f = Forecast(date=t)
		self.assertEqual(f.__str__(),t.strftime("%Y-%m-%d"))

class IndexViewTests(TestCase):

	def test_not_logged_in(self):
		"""
		Arriving on the landing page while not authenticated
		"""
		response = self.client.get(reverse('main:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, "Please register an account or log in.")


class ResultsViewTests(TestCase):

	def test_not_logged_in(self):
		"""
		Arriving on the landing page while not authenticated
		"""
		response = self.client.get(reverse('main:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response, "Please register an account or log in.")