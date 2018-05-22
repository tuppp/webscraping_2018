# -*- coding: utf-8 -*-
"""
Rest Client for getting openweathermap.org data
# username franz.1@campus.tu-berlin.de pw: passwort12

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

dateString = datetime.datetime.today().strftime('%Y-%m-%d');
localJsonSavePath = "openweather"+dateString+".txt";
websiteName = "http://api.openweathermap.org";

def kelvin_to_celcius(k_temp):
        return (k_temp - 273.15)
def meter_per_second_to_km_per_h(speed):
    return 3.6 * speed;

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
    returnList = [];

    file = saveModel.saveData();

    for url in urls:
        myResponse = requests.get(url);

        
        if(myResponse.ok):
            obj = myResponse.json(); 

            #save everything locally
            #if (os.path.exists(localJsonSavePath)):
            #    with open(localJsonSavePath, 'a') as outfile:
            #        json.dump(obj, outfile);
            #else:
            #    with open(localJsonSavePath, 'w') as outfile:
            #        json.dump(obj, outfile);
            
            lat  = obj["city"]["coord"]["lat"];
            lang = obj["city"]["coord"]["lon"];
            stadt = obj["city"]["name"];
            #print(stadt,lat,lang);
            obj = obj["list"];
            
            
            #print(obj[0]);
            
            for entry in obj:
                
                
                timestamp = entry["dt"];
                temperatur = kelvin_to_celcius(entry["main"]["temp"]);
                mintemperatur = kelvin_to_celcius(entry["main"]["temp_min"]);
                maxtemperatur = kelvin_to_celcius(entry["main"]["temp_max"]);
                windgeschwindigkeit = entry["wind"]["speed"];
                windgeschwindigkeit = meter_per_second_to_km_per_h(windgeschwindigkeit);
                luftdruck = entry["main"]["grnd_level"];
                
                websiteNameShort = "openweathermaporg";
                #save relevant data to csv file
#==============================================================================
#                 print(websiteNameShort, websiteName, 
#                                    time.time(), timestamp,      
#                                     None, stadt,
#                                    temperatur, None,None, 
#                                    None, windgeschwindigkeit, 
#                                    luftdruck, None, 
#                                    mintemperatur, maxtemperatur, 
#                                    None, None);
#==============================================================================

                file.save(websiteNameShort, websiteName,
                          time.time(), float(timestamp),
                          None, stadt,
                          float(temperatur), None, None,
                          None, float(windgeschwindigkeit),
                          float(luftdruck), None,
                          float(mintemperatur), float(maxtemperatur),
                          None, None)

                #print(returnListEntry);
                #returnList.append(returnListEntry);
            #return returnList;

        
        else:
          # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status();

    file.csvfile.close()

#start
getOpenWeatherMapData();