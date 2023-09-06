# connecting to api
from cmath import cos, sin
import math
import sympy
from sympy import sqrt, Symbol, S
import pip._vendor.requests
import json
response_API = pip._vendor.requests.get('http://api.open-notify.org/iss-now.json')
#print(response_API.status_code)

# getting data from api
data = response_API.text
station_location = json.loads(data)
location = station_location

# values for latitude and longitude of space station - converted to float so they can be input
stationlatitude = ((location['iss_position']['latitude']))
stationlat = (float(stationlatitude))
stationlongitude = ((location['iss_position']['longitude']))
stationlng = (float(stationlongitude))

# latitude and longitude of home
homelat = input("Input the latitude of your house:")
homelat = float(homelat)
homelng = input("Input the longitude of your house:")
homelng = float(homelng)

# difference between latitude and longitude
diflat = homelat - stationlat
diflng = homelng - stationlng

# equation for distance between cities and station
radius = 3963
x = math.sin(diflat / 2)**2 + math.sin(diflng / 2)**2 * math.cos(homelat) * math.cos(stationlat)
y = 2 * math.atan2(math.sqrt(x), math.sqrt(1 - x))
dist = radius * y
distance = int(dist)
print("Your house is" ,(distance), "miles from the space station")