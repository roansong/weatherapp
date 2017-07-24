====================
Weather24 Forecast
====================

This app allows the user to create an account, log in, and view 7-day forecasts provided by Weather24. Registered users can access and edit the data through a REST API.

I couldn't figure out how to get the package manager working how I wanted it, so some manual installation is required.


You should have the following directory structure:
current_dir/
----LICENSE
----README.rst
----requirements.txt
----byte_orbit/	
--------manage.py
--------byte_orbit/
------------__init__.py
------------settings.py
------------urls.py
------------wsgi.py
--------main/
------------__init__.py
------------admin.py
------------apps.py
------------forms.py
------------models.py
------------serializers.py
------------tests.py
------------urls.py
------------utils.py
------------views.py
------------migrations/
----------------__init__.py
----------------0001_initial.py
------------static/
----------------main/
--------------------styles.css
------------templates/
----------------polls/
--------------------detail.html
--------------------index.html
--------------------results.html



Quick start
-----------

1. Make sure you have the correct packages installed (I recommend running a virtualenv):

	pip install -r requirements.txt

2. Ensure that all databases are clean and healthy by running the following commands

	python manage.py flush

	python manage.py makemigrations

	python manage.py migrate

	python manage.py createsuperuser (fill in the details for your admin account)

	python manage.py test

	python manage.py runserver


3. Visit http://localhost:8000/ and enjoy the site

N.B. some important links: 
http://localhost:8000/ (home). You can get here by clicking the title of most pages.
http://localhost:8000/forecasts (API). Here you can edit the forecast data if you are logged in.
http://localhost:8000/weather (results). This page shows and formats the forecasts for you. 3 per page.
You can navigate using the "Next" and "Previous" buttons, or go directly to a results page by going to
http://localhost:8000/weather/2 where 2 is the desired page number.
I recommend trying http://localhost:8000/weather/?per_page=10 to see more forecasts at once.
