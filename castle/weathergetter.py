import requests
import json

def get_weather():
	r = requests.get('http://api.weatherapi.com/v1/current.json?key=39c2db6d1d55448d8ec105506220104&q=manchester&aqi=no')
	
	if r.status_code == 200:
	    data = json.loads(r.text)
	    data = data['current']
	
	    tempc = data['temp_c']
	    condition = data['condition']['text']
	    wind = data['wind_mph']
	    rain = data['precip_mm']
	
	    markup = "&#127777;{tmp}C&nbsp;&nbsp;"\
	            "&#128168;{wnd}mph&nbsp;&nbsp;"\
	            "&#128167;{ran}mm&nbsp;&nbsp;"\
	            "&#127774;{cond}".format(tmp=tempc, wnd=wind, ran=rain, cond=condition)
	
	    return markup
	else:
	    return "Error getting weather data"
