"""
Rest Client for getting openweathermap.org data
use getOpenWeatherMapData();

username franz.1@campus.tu-berlin.de pw: passwort12

@author:
alexander franz 358870
daniel hartung 338991    
"""

import requests
import datetime
import os
import json
import time
import saveCSVModel as saveModel
#import pdb

#names and paths for saving data
dateString = datetime.datetime.today().strftime('%Y-%m-%d');
localJsonSavePath = "openweather"+dateString+".txt";
websiteName = "http://api.openweathermap.org";
websiteNameShort = "openweathermaporg";


#functions for  converting units to metric system
def kelvin_to_celcius(k_temp):
        return (k_temp - 273.15)
def meter_per_second_to_km_per_h(speed):
    return 3.6 * speed;

#saves raw json response for backup purposes -> maybe use other parts later on?
def save_raw_json_response(obj):
    if not os.path.exists("raw_data"):
        os.makedirs("raw_data")

    if (os.path.exists("raw_data/" + localJsonSavePath)):
        with open("raw_data/" + localJsonSavePath, 'a') as outfile:
            json.dump(obj, outfile);
    else:
        with open("raw_data/" +localJsonSavePath, 'w') as outfile:
            json.dump(obj, outfile);

#extracts all the data out of json and saves it 
def extract_and_save_data(obj, file):
    stadt = obj["city"]["name"];
    obj = obj["list"];
    
    for entry in obj:
        #extract data from response
        timestamp = entry["dt"];
        temperatur = kelvin_to_celcius(entry["main"]["temp"]);
        mintemperatur = kelvin_to_celcius(entry["main"]["temp_min"]);
        maxtemperatur = kelvin_to_celcius(entry["main"]["temp_max"]);
        windgeschwindigkeit = entry["wind"]["speed"];
        windgeschwindigkeit = meter_per_second_to_km_per_h(windgeschwindigkeit);
        luftdruck = entry["main"]["grnd_level"];
        
        
        #save relevant data to csv file
        file.save(websiteNameShort, websiteName,
                  time.time(), float(timestamp),
                  None, stadt,
                  float(temperatur), None, None,
                  None, float(windgeschwindigkeit),
                  float(luftdruck), None,
                  float(mintemperatur), float(maxtemperatur),
                  None, None)


#main
def getOpenWeatherMapData():

    file_object = open("ZIP_Codes", "r")
    zip_codes = file_object.readlines()
    url = "http://api.openweathermap.org/data/2.5/forecast?APPID=428ef9d699cb5963b396bd10215f2d3f&zip="
    url_appendix = ",de"
    file = saveModel.saveData()

    #do API call for all locations
    for index,zip_code in enumerate(zip_codes):
        if index % 60 == 0 and index != 0:
           time.sleep(61)
        myResponse = requests.get(url + zip_code.rstrip() + url_appendix)

        if(myResponse.ok):
            obj = myResponse.json()
            save_raw_json_response(obj)
            extract_and_save_data(obj,file)
        else:
            #If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status()

    file.csvfile.close()

def run():
    getOpenWeatherMapData()