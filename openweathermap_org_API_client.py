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
    
    print("wir holen daten von openweathermap.org per API")
    urls = [
    "http://api.openweathermap.org/data/2.5/forecast?id=2950159&APPID=428ef9d699cb5963b396bd10215f2d3f", #berlin
    "http://api.openweathermap.org/data/2.5/forecast?id=6547395&APPID=428ef9d699cb5963b396bd10215f2d3f",#hamburg
    "http://api.openweathermap.org/data/2.5/forecast?id=2867714&APPID=428ef9d699cb5963b396bd10215f2d3f",#münchen
    "http://api.openweathermap.org/data/2.5/forecast?id=2886242&APPID=428ef9d699cb5963b396bd10215f2d3f",#köln
    "http://api.openweathermap.org/data/2.5/forecast?id=2925533&APPID=428ef9d699cb5963b396bd10215f2d3f",#frankfurt am main
    "http://api.openweathermap.org/data/2.5/forecast?id=2825297&APPID=428ef9d699cb5963b396bd10215f2d3f",#stuttgart
    "http://api.openweathermap.org/data/2.5/forecast?id=2934245&APPID=428ef9d699cb5963b396bd10215f2d3f",#düsseldorf
    "http://api.openweathermap.org/data/2.5/forecast?id=2935517&APPID=428ef9d699cb5963b396bd10215f2d3f",#dortmund
    "http://api.openweathermap.org/data/2.5/forecast?id=2928809&APPID=428ef9d699cb5963b396bd10215f2d3f",#essen
    "http://api.openweathermap.org/data/2.5/forecast?id=2879139&APPID=428ef9d699cb5963b396bd10215f2d3f",#leipzig
    ];
    file = saveModel.saveData();

    #do API call for all locations
    for url in urls:
        myResponse = requests.get(url);

        if(myResponse.ok):
            obj = myResponse.json(); 
            save_raw_json_response(obj);
            extract_and_save_data(obj,file);
            
        else:
          # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status();

    file.csvfile.close()


def run():
    getOpenWeatherMapData()


