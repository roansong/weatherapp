from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Weather
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):

	if(request.user.is_authenticated):
		context={'user' : request.user}
		return render(request, 'welcome/forecasts.html', context)

	return render(request, 'welcome/index.html', context=None)

def register(request):

	
	user = User.objects.create_user(username=request.POST['email'],email=request.POST['email'],password=request.POST['password'])

	return render(request, 'welcome/login.html', context=None)


def login(request):

	user = authenticate(username=request.POST['email'], password=request.POST['password'])
	if user is not None:
	    return render(request, 'welcome/forecasts.html', context=None)
	else:
	    return render(request, 'welcome/index.html', context=None)

	

def WeatherData(request):
	page = 1
	page_length = 3

	# if(page <=0):
	# 	return Http404
	
	# find most recent weather entries
	index = page_length*(page-1)
	weather_data = Weather.objects.order_by('-date')[:]

	context = {'weather_data': weather_data}
	return render(request, 'welcome/forecasts.html', context)