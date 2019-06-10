#pip install reverse_geocoder
#pip install pprint
from django.shortcuts import render
import urllib, json
import geocoder
import reverse_geocoder as rg
import random
def home(request):

    # Current Location
    g = geocoder.ip('me')
    latlon = g.latlng
    result = rg.search((latlon[0],latlon[1]))

    # Weather
    url = "https://api.darksky.net/forecast/9229258e1491d592cda918516dd382f9/{},{}?exclude=minutely,hourly,daily,alerts,flags&units=auto".format(latlon[0],latlon[1])
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    # Compliments
    compliment = ['You Look Stunning!','Hey, Gorgeous!', 'You look Sexy!', 'Synonym for beauty is you!', 'Fair and Lovely!']
    chooser = random.randint(0,len(compliment)-1)
    final_data = {'temperature' : round(int(data['currently']['temperature'])), 'summary' : data['currently']['summary'], 'place' : result[0]['name'] , 'compliment' : compliment[chooser] } 
    return render(request, 'base.html', context=final_data)
