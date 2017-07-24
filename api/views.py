from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ForecastSerializer
from .models import Forecast
import requests
import json
from django.contrib.auth.mixins import LoginRequiredMixin

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

