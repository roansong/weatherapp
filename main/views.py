from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from main.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from api.models import Forecast
from api.utils import load_forecasts

# Create your views here.

class IndexView(TemplateView):
	template_name = "main/index.html"

@login_required
def results(request, page=0):	
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