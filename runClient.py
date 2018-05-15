import pdb

from OpenWheatherMapRestClient import *
from saveCSVModel import *





''' Test: OpenWeatherMapRestClient '''
stadt,timestamp,temperatur,mintemperatur,maxtemperatur,windgeschwindigkeit,luftdruck,niederschlagswahrscheinlichkeit = getOpenWeatherMapData()
pdb.set_trace()
save(url="https://openweathermap.org/", timestamp=1526388799.745863, postleitzahl=None, stadt=stadt, temperatur=temperatur, niederschlagswahrscheinlichkeit=niederschlagswahrscheinlichkeit, windgeschwindigkeit=windgeschwindigkeit,luftdruck=luftdruck, mintemperatur=mintemperatur, maxtemperatur=maxtemperatur)
pdb.set_trace()