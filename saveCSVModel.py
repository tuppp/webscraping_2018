import unittest
import validators
import re
import pdb
import os
import csv
import datetime
import time
def test(hi):
    pdb.set_trace()

def save(url, timestamp, timestamppred, postleitzahl=None, stadt=None, temperatur=None, niederschlagswahrscheinlichkeit=None, niederschlag=None, windgeschwindkeit=None,
         luftdruckground=None, luftdrucksea=None, mintemperatur=None, maxtemperatur=None, sonnenstunden=None, bewölkung=None):
    """save information to csv which is later saved to database

        url: String
        timestamp: float
        timestamppred: float
        postleitzahl: String len=5
        stadt: String
        temperatur(in Celsius): float [-100,200]
        niederschlagswahrscheinlichkeit: float [0,100]
        niederschlag: String
        windgeschwindigkeit(in km/h): float [0,500]
        luftdruckground(in hPa on groundlevel): float [0,1050]
        luftdrucksea(in hPa on sealevel): float [0,1050]
        mintemperatur(in Celsius): float [-100,200]
        maxtemperatur(in Celsius): float [-100,200]
        sonnenstunden: float [0,24]
        bewölkung(in h): float [0,24]

       """


    '''Exception Handling'''

    if type(url) != str:
        raise Exception('url ist kein String')

    if not validators.url(url):
        raise Exception('Deine Url ist keine Url. Bashed!!')

    #if re.match('\d{2}:\d{2}:\d{2}', timestamp):
    #   raise Exception('Timestamp ist nicht korrekt.')

    if type(timestamp) != float:
        raise Exception("Timestamp kein Float")


    if (postleitzahl==None and stadt==None):
        raise Exception("Bitte gebe eine Stadt oder eine PLZ an!")

    if postleitzahl!=None:
        if type(postleitzahl) != str:
            raise Exception('postleitzahl ist kein String')

        if len(postleitzahl)!=5:
            raise Exception("Postleitzahl geht nur mit 5 Ziffern")

    if temperatur is None:
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
        raise Exception("Max und Mintemperatur können nur paarweise existieren.")

    if (stadt!=None and  type(stadt)!=str):
        raise Exception("Stadt ist kein String")

    if niederschlagswahrscheinlichkeit is not None:
        if type(niederschlagswahrscheinlichkeit)!=float:
            raise Exception('niederschlagswahrscheinlichkeit kein float')

        if niederschlagswahrscheinlichkeit < 0.0 or niederschlagswahrscheinlichkeit > 100.0:
            raise Exception('niederschlagswahrscheinlichkeit nicht zwischen 0 und 100')

    if niederschlag != None and type(niederschlag) != str:
        raise Exception('niederschlag ist kein String')

    if windgeschwindkeit is not None:
        if type(windgeschwindkeit)!=float:
            raise Exception('windgeschwindigkeit kein float')

        if windgeschwindkeit < 0 or windgeschwindkeit > 500:
            raise Exception('windgeschwindigkeit nicht zwischen 0 und 500')

    if luftdruckground is not None:
        if type(luftdruckground)!=float:
            raise Exception('luftdruckground ist kein float')

        if luftdruckground < 0 or luftdruckground > 1050:
            raise Exception('luftdruck ist nicht zwischen 0 und 1050')

    if luftdrucksea is not None:
        if type(luftdrucksea) != float:
            raise Exception('luftdrucksea ist kein float')

        if luftdrucksea < 0 or luftdrucksea > 1050:
            raise Exception('luftdruck ist nicht zwischen 0 und 1050')

    if sonnenstunden is not None:
        if type(sonnenstunden) != float:
            raise Exception('sonnenstunden ist kein float')

        if sonnenstunden < 0.0 or sonnenstunden > 24.0:
            raise Exception('sonnenstunden ist nicht zwischen 0 und 24')

    if bewölkung is not None:
        if type(bewölkung) != float:
            raise Exception('sonnenstunden ist kein float')

        if bewölkung < 0.0 or bewölkung > 24.0:
            raise Exception('sonnenstunden ist nicht zwischen 0 und 24')

    format=time.localtime(timestamp)
    filename=str(format.tm_mday)+"-"+str(format.tm_mon)+"-"+ str(format.tm_year)
    csvfile=None
    csvwriter=None
    if os.path.exists(filename):
        csvfile=open(filename,'a')
        csvwriter = csv.writer(csvfile, delimiter=',')
    else:
        csvfile=open(filename,'w')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["url", "timestamp", "timestamppred", "postleitzahl", "stadt", "temperatur", "niederschlagswahrscheinlichkeit", "niederschlag", "windgeschwindkeit",
         "luftdruckground", "luftdrucksea", "mintemperatur", "maxtemperatur", "sonnenstunden", "bewölkung"])

    csvwriter.writerow(
        [url, timestamp, timestamppred, postleitzahl, stadt, temperatur, niederschlagswahrscheinlichkeit, niederschlag, windgeschwindkeit,
         luftdruckground, luftdrucksea, mintemperatur, maxtemperatur, sonnenstunden, bewölkung])


    csvfile.close()



    ''' check day 
    - if day already: add to existing file

    else: same new file
    '''



    ''' save to CSV '''



save("http://www.google.de", timestamp=time.time(),timestamppred=time.time(),postleitzahl= "61231",stadt="Berlin",  maxtemperatur=23.4, niederschlagswahrscheinlichkeit=80.20, windgeschwindkeit=200.0,mintemperatur= 10.0 )


'''



class TestStringMethods(unittest.TestCase):
    
    
    def test_plzkorrekt(selfs):
        save()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
'''
