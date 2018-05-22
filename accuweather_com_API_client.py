# -*- coding: utf-8 -*-
"""
Rest Client for getting a data from accuweather.org
use getAccuWeatherData()

this code is not pretty yet, will be done next week

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
import validators

websiteName = "www.accuweather.com";
dateString = datetime.datetime.today().strftime('%Y-%m-%d');
localJsonSavePath = "accuweather"+dateString+".txt";


def getAccuWeatherData():
    print("wir holen daten von accuweather per API")
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
    returnList = [];

    file = saveModel.saveData();

    for index,url in enumerate(urls):
        myResponse = requests.get(url);
        time.sleep(5);
        
        if(myResponse.ok):
            obj = myResponse.json(); 

#==============================================================================
#             #save everything locally
#             if (os.path.exists(localJsonSavePath)):
#                 with open(localJsonSavePath, 'a') as outfile:
#                     json.dump(obj, outfile);
#             else:
#                 with open(localJsonSavePath, 'w') as outfile:
#                     json.dump(obj, outfile);
#==============================================================================
            
            
            stadt = staedte[index];
            
            #print(stadt, dateString);
            #print("stadt","abfragedatum","timestamp","temp", "mintemp", "maxtemp", "wind","luftdruck","regen%","bewoelkung","sonnenstunden" );
            obj = obj["DailyForecasts"];
            
            
            
            for entry in obj:
                #print(entry);
                
                timestamp = entry["EpochDate"];
                temperatur = "None";
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
                          float(sonnenstunden), str(bewoelkung))

               # print(websiteNameShort,websiteName,
               #                   time.time(), float(timestamp),
               #                   None, stadt,
               #                 None, float(niederschlagswahrscheinlichkeit), float(niederschlagsmenge),
               #                None, float(windgeschwindigkeit),
               #               None, None,
               #              float(mintemperatur), float(maxtemperatur),
               #    float(sonnenstunden), str(bewoelkung))
            #return 1;
        
        else:
          # If response code is not ok (200), print the resulting http error code with description
           # print("hatte nisch jeklappt"+staedte[index])
            myResponse.raise_for_status()

    file.csvfile.close()

#start
getAccuWeatherData();