import requests
import json
from geopy.geocoders import Nominatim

user_input = raw_input("Enter a location: ")

geolocator = Nominatim()
location = geolocator.geocode(user_input)
longitude = str(location.longitude).decode('utf8')
latitude = str(location.latitude).decode('utf8')

DARK_SKY_API_KEY="70573f8f45cd15ab543902b7d5540fcb"
DARK_SKY_API_KEY = str(DARK_SKY_API_KEY).decode('utf8')

response = requests.get('https://api.darksky.net/forecast/'+DARK_SKY_API_KEY+'/'+longitude+','+latitude)

json_data = json.loads(response.text)
print(json_data, response)
