from django.shortcuts import render
from rest_framework import generics
from .serializers import ForecastSerializer
from .models import Forecast
import requests
import json

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new forecast."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""Class to handle GET, PUT and DELETE requests"""
	queryset = Forecast.objects.all()
	serializer_class = ForecastSerializer

