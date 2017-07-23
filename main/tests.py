from django.test import TestCase
from django.urls import reverse

# Create your tests here.
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