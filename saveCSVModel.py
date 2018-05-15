import numpy as np
import unittest
import validators
import re
import pdb
import os
import csv
import datetime
def test(hi):
    pdb.set_trace()

def save(url, timestamp, postleitzahl=None, stadt=None, temperatur=None, niederschlagswahrscheinlichkeit=None, windgeschwindigkeit=None,
         luftdruck=None, mintemperatur=None, maxtemperatur=None):
    """save information to csv which is later saved to database
       wahrscheinlichkeiten [0,100]
       windgeschwindigkeit [km/h]
       luftdruck  [hPa] - groundlevel
       temperatur [Grad Celsius]

       timestamp: string
       """


    '''Exception Handling'''

    if type(url) != str:
        raise Exception('url ist kein String')

    if not validators.url(url):
        raise Exception('Deine Url ist keine Url. Bashed!!')

    #if re.match('\d{2}:\d{2}:\d{2}', timestamp):
    #   raise Exception('Timestamp ist nicht korrekt.')

    if type(timestamp) != float:
        raise Exception("Timestamp ist kein Float")

    if (postleitzahl==None and stadt==None):
        raise Exception("Bitte gebe eine Stadt oder eine PLZ an!")

    if (postleitzahl!=None and len(postleitzahl)!=5):
        raise Exception("Postleitzahl geht nur mit 5 Ziffern")

    if  temperatur is None:
        if mintemperatur == None:
                if maxtemperatur == None:
                    raise Exception("Bitte geben sie eine Temperatur oder eine Min- und Maxtemperatur an")

    if temperatur is not None:
        if type(temperatur) == float:
            if(temperatur>200.0 or temperatur <-100.0):
                raise Exception("Die Temperatur ist nicht realistisch")
        else:
            raise Exception("Temperatur ist kein Float")

    if mintemperatur is not None:
        if type(mintemperatur) == float:
            if mintemperatur>200.0 or mintemperatur <-100.0:
                raise Exception("Die minimal Temperatur ist nicht realistisch")
        else:
            raise Exception("Die minimal Temperatur ist kein Float")

    if maxtemperatur is not None:
        if type(maxtemperatur) == float:
            if (maxtemperatur > 200.0 or maxtemperatur < -100.0):
                raise Exception("Die maximal Temperatur ist nicht realistisch")
        else:
            raise Exception("Die maximal Temperatur ist kein Float")

    if (maxtemperatur is None and type(mintemperatur)==float) or ( mintemperatur is None and type(maxtemperatur)==float):
        raise Exception("Max und Mintemperatur koennen nur paarweise existieren.")

    if (stadt!=None and  type(stadt)!=str):
        raise Exception("Stadt ist kein String")

    if niederschlagswahrscheinlichkeit is not None:
        if type(niederschlagswahrscheinlichkeit)!=float:
            raise Exception('niederschlagswahrscheinlichkeit kein float')


        if niederschlagswahrscheinlichkeit < 0.0 or niederschlagswahrscheinlichkeit > 100.0:
            raise Exception('niederschlagswahrscheinlichkeit nicht zwischen 0 und 100')

    if windgeschwindkeit is not None:
        if type(windgeschwindkeit)!=float:
            raise Exception('windgeschwindigkeit kein float')

        if windgeschwindkeit < 0 or windgeschwindkeit > 500:
            raise Exception('windgeschwindigkeit nicht zwischen 0 und 500')

    if luftdruck is not None:
        if type(luftdruck)!=float:
            raise Exception('luftdruck ist kein float')

        if luftdruck < 0 or luftdruck > 1050:
            raise Exception('luftdruck ist nicht zwischen 0 und 1050')
    filename=str(timestamp.day) + "-" + str(timestamp.month)+"."+ str(timestamp.year)

    csvfile=None
    csvwriter=None
    print(filename)
    if os.path.exists(filename):
        csvfile=open(filename,'a')
        csvwriter = csv.writer(csvfile, delimiter=',')
    else:
        csvfile=open(filename,'w')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["url", "timestamp", "postleitzahl", "stadt", "temperatur", "niederschlagswahrscheinlichkeit", "windgeschwindkeit",
         "luftdruck", "mintemperatur", "maxtemperatur"])

    csvwriter.writerow(
        [url, timestamp, postleitzahl, stadt, temperatur, niederschlagswahrscheinlichkeit, windgeschwindkeit,
         luftdruck, mintemperatur, maxtemperatur])

    csvfile.close()



    ''' check day 
    - if day already: add to existing file

    else: same new file
    '''



    ''' save to CSV '''




