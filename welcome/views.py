from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Weather

# Create your views here.
class HomePageView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
    template_name = 'index.html'

class RegistrationView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
    template_name = 'registration.html'

class LoginView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
    template_name = 'login.html'

class LoggedInView(TemplateView):
	template_name = 'forecasts.html'





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