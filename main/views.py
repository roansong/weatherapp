from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request):

	return render(request, 'main/index.html', context=None)

class IndexView(TemplateView):
	template_name = "main/index.html"

class ResultsView(TemplateView):	
	template_name = "main/results.html"