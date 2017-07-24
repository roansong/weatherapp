import requests
import re
import json
from io import StringIO
import datetime
from django.utils import timezone
from .models import Forecast

# exec(open("./api/utils.py").read())

def get_data(cityId = '77107'):
	"""
	Function to get a 7 day forecast for cape town from weather24
	"""

	url = 'http://weather.news24.com/ajaxpro/TwentyFour.Weather.Web.Ajax,App_Code.ashx'  # noqa
	data = {'cityId': cityId}
	headers = {
		'X-AjaxPro-Method': 'GetForecast7Day',
	}

	response = requests.post(url, headers=headers, data=json.dumps(data))
	j = clean_json(response.text)
	j = StringIO(j)
	j = json.load(j)
	return j

def clean_json(text):
	"""
	Dirty JSON needs to be cleaned
	"""
	
	# trailing ;/* needs to be chopped off
	text = text[:-3]

	# in: "Date":new Date(Date.UTC(2017,6,22,22,0,0,0))
	# out: "Date":"2017-07-22"

	pattern = re.compile(r'new Date\(Date\.UTC\(\d*,\d*,\d*,\d*,\d*,\d*,\d*\)\)')
	date_in = re.compile(r'\d*,\d*,\d*,\d*,\d*,\d*,\d*')
	full_str = re.findall(pattern,text)
	date_data = re.findall(date_in,text)
	
	for i in date_data:
		# convert date into better format and then replace in the string
		# note that month and day are off by 1, and need to be changed
		lst = i.split(',')
		lst[1] = str(int(lst[1]) + 1)
		lst[2] = str(int(lst[2]) + 1)
		i = ','.join(lst)
		repl = '"'+eval('datetime.datetime('+i+')').date().__str__()+'"'
		text = re.sub(pattern, repl, text, 1)
	return text

def load_forecasts():
	"""
	Load the forecast data into the database, and clean out old entries
	"""
	response = get_data()
	for f in response['Forecasts']:
		date = f['Date']
		qset = Forecast.objects.filter(date=date)
		if not (qset.exists()):
			min_temp = int(f['LowTemp']) if not f['LowTemp'] == None else 0
			max_temp = int(f['HighTemp']) if not f['HighTemp'] == None else 0
			wind = int(f['WindSpeed']) if not f['WindSpeed'] == None else 0
			rain = int(f['Rainfall']) if not f['Rainfall'] == None else 0
			c = Forecast(date=date, min_temp=min_temp, max_temp=max_temp, wind=wind, rain=rain)
			c.save()