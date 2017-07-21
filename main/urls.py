from django.conf.urls import url
from . import views


app_name = 'main'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^weather/$', views.ResultsView.as_view(), name='results'),
]