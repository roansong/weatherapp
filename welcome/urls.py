# howdy/urls.py
from django.conf.urls import url
from . import views


app_name = 'weather'

urlpatterns = [
    # url(r'^$', views.WeatherData.as_view()),
    url(r'^$', views.index, name='index'),
    url(r'^forecasts/$', views.WeatherData, name='weather'),
    url(r'^register/$', views.register, name='register'),
]