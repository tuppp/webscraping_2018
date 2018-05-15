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

def save(websitename, url, timestamp, timestamppred, postleitzahl=None, stadt=None, temperatur=None, niederschlagswahrscheinlichkeit=None, niederschlagsmenge=None, niederschlag=None, windgeschwindkeit=None,
         luftdruckground=None, luftdrucksea=None, mintemperatur=None, maxtemperatur=None, sonnenstunden=None, bewoelkung=None):
    """save information to csv which is later saved to database

        websitename(Bsp.: https://wetter.com als wettercom): String
        url: String
        timestamp: Float
        timestamppred: Float
        postleitzahl: String len=5
        stadt: String
        temperatur(in Celsius): Float [-100,200]
        niederschlagswahrscheinlichkeit: Float [0,100]
        niederschlagsmenge(in mm): Float [0,2000]
        niederschlag: String
        windgeschwindigkeit(in km/h): Float [0,500]
        luftdruckground(in hPa on groundlevel): Float [0,1050]
        luftdrucksea(in hPa on sealevel): Float [0,1050]
        mintemperatur(in Celsius): Float [-100,200]
        maxtemperatur(in Celsius): Float [-100,200]
        sonnenstunden: Float [0,24]
        bewoelkung: Sting

       """


    '''Exception Handling'''

    if type(websitename) != str:
        raise Exception('websitename ist kein String')

    if type(url) != str:
        raise Exception('url ist kein String')

    if not validators.url(url):
        raise Exception('Deine Url ist keine Url. Bashed!!')

    #if re.match('\d{2}:\d{2}:\d{2}', timestamp):
    #   raise Exception('Timestamp ist nicht korrekt.')

    if type(timestamp) != float:
        raise Exception("timestamp kein Float")

    if type(timestamppred) != float:
        raise Exception("timestamppred ist kein Float")


    if (postleitzahl==None and stadt==None):
        raise Exception("Bitte gebe eine Stadt oder eine PLZ an!")

    if postleitzahl!=None:
        if type(postleitzahl) != str:
            raise Exception('postleitzahl ist kein String')

        if len(postleitzahl)!=5:
            raise Exception("postleitzahl geht nur mit 5 Ziffern")

    if temperatur is None:
        if mintemperatur == None:
                if maxtemperatur == None:
                    raise Exception("Bitte geben sie eine Temperatur oder eine Min- und Maxtemperatur an")

    if temperatur is not None:
        if type(temperatur) == float:
            if(temperatur>200.0 or temperatur <-100.0):
                raise Exception("temperatur ist nicht zwischen -100 und 200")
        else:
            raise Exception("temperatur ist kein Float")

    if mintemperatur is not None:
        if type(mintemperatur) == float:
            if mintemperatur>200.0 or mintemperatur <-100.0:
                raise Exception("mintemperatur ist nicht zwischen -100 und 200")
        else:
            raise Exception("mintemperatur ist kein Float")

    if maxtemperatur is not None:
        if type(maxtemperatur) == float:
            if (maxtemperatur > 200.0 or maxtemperatur < -100.0):
                raise Exception("maxtemperatur nicht zwischen -100 und 200")
        else:
            raise Exception("maxtemperatur ist kein Float")

    if (maxtemperatur is None and type(mintemperatur)==float) or ( mintemperatur is None and type(maxtemperatur)==float):
        raise Exception("Max und Mintemperatur können nur paarweise existieren.")

    if (stadt!=None and  type(stadt)!=str):
        raise Exception("stadt ist kein String")

    if niederschlagswahrscheinlichkeit is not None:
        if type(niederschlagswahrscheinlichkeit)!=float:
            raise Exception('niederschlagswahrscheinlichkeit kein Float')

        if niederschlagswahrscheinlichkeit < 0.0 or niederschlagswahrscheinlichkeit > 100.0:
            raise Exception('niederschlagswahrscheinlichkeit nicht zwischen 0 und 100')

    if niederschlagsmenge is not None:
        if type(niederschlagsmenge) != float:
            raise Exception('niederschlagsmenge ist kein Float')

        if niederschlagsmenge < 0 or niederschlagsmenge > 2000:
            raise Exception('niederschlagsmenge ist nicht zwischen 0 und 2000')

    if niederschlag != None and type(niederschlag) != str:
        raise Exception('niederschlag ist kein String')

    if windgeschwindkeit is not None:
        if type(windgeschwindkeit)!=float:
            raise Exception('windgeschwindigkeit kein Float')

        if windgeschwindkeit < 0 or windgeschwindkeit > 500:
            raise Exception('windgeschwindigkeit nicht zwischen 0 und 500')

    if luftdruckground is not None:
        if type(luftdruckground)!=float:
            raise Exception('luftdruckground ist kein Float')

        if luftdruckground < 0 or luftdruckground > 1050:
            raise Exception('luftdruck ist nicht zwischen 0 und 1050')

    if luftdrucksea is not None:
        if type(luftdrucksea) != float:
            raise Exception('luftdrucksea ist kein Float')

        if luftdrucksea < 0 or luftdrucksea > 1050:
            raise Exception('luftdruck ist nicht zwischen 0 und 1050')

    if sonnenstunden is not None:
        if type(sonnenstunden) != float:
            raise Exception('sonnenstunden ist kein Float')

        if sonnenstunden < 0.0 or sonnenstunden > 24.0:
            raise Exception('sonnenstunden ist nicht zwischen 0 und 24')

    if bewoelkung is not None and type(bewoelkung) != str:
        raise Exception('bewölkung ist kein String')

    format=time.localtime(timestamp)
    filename=str(format.tm_mday)+"-"+str(format.tm_mon)+"-"+ str(format.tm_year) +"_" + websitename
    csvfile=None
    csvwriter=None
    if os.path.exists(filename):
        csvfile=open(filename,'a')
        csvwriter = csv.writer(csvfile, delimiter=',')
    else:
        csvfile=open(filename,'w')
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["url", "timestamp", "timestamppred", "postleitzahl", "stadt", "temperatur", "niederschlagswahrscheinlichkeit", "niederschlagsmenge", "niederschlag", "windgeschwindkeit",
         "luftdruckground", "luftdrucksea", "mintemperatur", "maxtemperatur", "sonnenstunden", "bewoelkung"])

    csvwriter.writerow(
        [url, timestamp, timestamppred, postleitzahl, stadt, temperatur, niederschlagswahrscheinlichkeit, niederschlagsmenge, niederschlag, windgeschwindkeit,
         luftdruckground, luftdrucksea, mintemperatur, maxtemperatur, sonnenstunden, bewoelkung])


    csvfile.close()



    ''' check day 
    - if day already: add to existing file

    else: same new file
    '''



    ''' save to CSV '''



save("googlecom", "http://www.google.de", timestamp=time.time(),timestamppred=time.time(),postleitzahl= "61231",stadt="Berlin",  maxtemperatur=23.4, niederschlagswahrscheinlichkeit=80.20, windgeschwindkeit=200.0,mintemperatur= 10.0 )


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
