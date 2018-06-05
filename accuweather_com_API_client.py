# -*- coding: utf-8 -*-
"""
Rest Client for getting a data from accuweather.org
- using accuweather with zipcodes is close to impossible
- this client gets weather forecast for the 10 biggest cities in germany  and nothing else
- use getAccuWeatherData() to get data  or use (filename).run() 
- if api call doesnt work, we dont throw an error or anything we just carry on

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

websiteName = "http://www.accuweather.com";
dateString = datetime.datetime.today().strftime('%Y-%m-%d');
localJsonSavePath = "accuweather"+dateString+".txt";

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
def extract_and_save_data(obj, file,staedte,index):
    stadt = staedte[index];
            
    obj = obj["DailyForecasts"];
    for entry in obj:   
        timestamp = entry["EpochDate"];
        mintemperatur = entry["Temperature"]["Minimum"]["Value"];
        maxtemperatur = entry["Temperature"]["Maximum"]["Value"];
        sonnenstunden = entry["HoursOfSun"]
        windgeschwindigkeit = entry["Day"]["Wind"]["Speed"]["Value"];
        niederschlagswahrscheinlichkeit = entry["Day"]["RainProbability"];
        niederschlagsmenge = entry["Day"]["Rain"]["Value"];
        bewoelkung = entry["Day"]["CloudCover"]; 
        websiteNameShort = "accuweathercom";


        file.save(websiteNameShort,websiteName, 
                  time.time(), float(timestamp),
                  None, stadt,
                  None, float(niederschlagswahrscheinlichkeit), float(niederschlagsmenge),
                  None, float(windgeschwindigkeit),
                  None, None, 
                  float(mintemperatur), float(maxtemperatur),
                  float(sonnenstunden), str(bewoelkung));

#main
def getAccuWeatherData():
    #print("wir holen daten von accuweather per API")
    urls = [
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/178087?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true", #berlin
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/178556?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#hamburg
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/178086?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#münchen
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/180169?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#köln
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/168720?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#frankfurt am main
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/167220?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#stuttgart
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/170372?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#düsseldorf
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/170370?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#dortmund
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/170373?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true",#essen
    "http://dataservice.accuweather.com/forecasts/v1/daily/5day/171240?apikey=NWXSvpg68FDbYdNYneJnLWLZMZ5HwJu5&language=de&details=true&metric=true"#leipzig
    ];
    staedte = ["Berlin", "Hamburg", "Muenchen","Koeln","Frankfurt am Main", "Stuttgart", "Duesseldorf", "Dortmund", "Essen", "Leipzig"]

    #our own save function: saves everything into special csv file
    file = saveModel.saveData();

    #do API call for all locations
    for index,url in enumerate(urls):
        myResponse = requests.get(url);

        if(myResponse.ok):
            obj = myResponse.json(); 
            save_raw_json_response(obj);
            extract_and_save_data(obj,file,staedte,index);  
        #if http get didnt work somehow, we just ignore it        
        #this api doesnt want us to do bruteforce api calls,  we have to be patient ater each call
        time.sleep(5);
    #after doing all the api call calls an extracting all the data, close the csv and terminate
    file.close()

def run():
  getAccuWeatherData();


#start
#getAccuWeatherData();