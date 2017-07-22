from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    url(r'^forecasts/$', CreateView.as_view(), name="create"),
    url(r'^forecasts/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

# append the format of the data to every URL
urlpatterns = format_suffix_patterns(urlpatterns)