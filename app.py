import requests
import json
from geopy.geocoders import Nominatim

user_input = raw_input("Enter a location: ")

geolocator = Nominatim()
location = geolocator.geocode(user_input)
longitude = str(location.longitude)
latitude = str(location.latitude)
longitude = str(longitude).decode('utf8')
latitude = str(latitude).decode('utf8')

DARK_SKY_API_KEY="70573f8f45cd15ab543902b7d5540fcb"
DARK_SKY_API_KEY = str(DARK_SKY_API_KEY).decode('utf8')

response2 = requests.get('https://api.darksky.net/forecast/'+DARK_SKY_API_KEY+'/'+longitude+','+latitude)

json_data = json.loads(response2.text)
print(json_data)
print(response2)
