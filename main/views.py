from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from main.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

	return render(request, 'main/index.html', context=None)

class IndexView(TemplateView):
	template_name = "main/index.html"


class ResultsView(TemplateView):	
	template_name = "main/results.html"

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if(user is not None):
	            login(request, user)

	            return redirect('main:results')
            else:
            	return redirect('main:index')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})