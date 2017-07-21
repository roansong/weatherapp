from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Weather
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.







def index(request):

	if(request.user.is_authenticated):
		return WeatherData(request)
	return render(request, 'welcome/index.html', context=None)

def register(request):

	
	user = User.objects.create_user(username=request.POST['email'],email=request.POST['email'],password=request.POST['password'])



	return render(request, 'welcome/index.html', context={'registered':True})

def logout_req(request):
	logout(request)
	return render(request, 'welcome/index.html', context=None)

def login_req(request):
	
	username = request.POST['email'] if 'email' in request.POST else None
	password = request.POST['password'] if 'password' in request.POST else None

	
	if username is not None:
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			return WeatherData(request)
	return render(request, 'welcome/index.html', context=None)

	
@login_required
def WeatherData(request):
	
	page = request.POST['page'] if 'page' in request.POST else 1
	page_length = request.POST['page_length'] if 'page_length' in request.POST else 3


	# if(page <=0)?:
	# find most recent weather entries
	index = page_length*(page-1)
	weather_data = Weather.objects.order_by('-date')[index:index + page_length]

	context = {'weather_data': weather_data}
	return render(request, 'welcome/forecasts.html', context)