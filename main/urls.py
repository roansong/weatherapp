from django.conf.urls import url
from . import views


app_name = 'main'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^weather/$', views.results, name='results'),
    url(r'^weather/(?P<page>[0-9]+)/$', views.results, name='pages'),
]