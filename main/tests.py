from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

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