from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'main'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^weather/$', views.results, name='results'),
    url(r'^weather/(?P<page>[0-9]+)/$', views.results, name='pages'),
    url(r'^forecasts/$', views.CreateView.as_view(), name='create'),
	url(r'^forecasts/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
]

# append the format of the data to every URL
urlpatterns = format_suffix_patterns(urlpatterns)