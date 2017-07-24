from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from main.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Forecast
from .utils import load_forecasts

from rest_framework import generics, permissions
from .serializers import ForecastSerializer

import requests
import json
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(TemplateView):
	template_name = "main/index.html"

@login_required
def results(request, page=0):	
    """Weather display page"""

    if not (Forecast.objects.count() > 0):
        print('loading')
        load_forecasts()
    page_length = int(request.GET['per_page']) if 'per_page' in request.GET else 3


    page = int(page)
    
    ind = page*page_length
    query = Forecast.objects.all().order_by('-date')

    context = {
        'forecasts': query[ind:ind+page_length],
        'nextPage':page+1 if ind + page_length <= len(query) else -1,
        'prevPage':page-1,
        'page':page,
        }

    return render(request, 'main/results.html', context)

def register(request):
    """Register and create a user if a valid form is submitted"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

class CreateView(LoginRequiredMixin, generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    login_url = '/login/'
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        """Save the post data when creating a new forecast."""
        serializer.save()


class DetailsView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    """Class to handle GET, PUT and DELETE requests"""
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    login_url = '/login/'
    permission_classes = (permissions.IsAuthenticated,)