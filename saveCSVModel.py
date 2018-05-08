import numpy as np

import unittest




def save(url, timestamp, postleitzahl, temperatur, niederschlagswahrscheinlichkeit, windgeschwindkeit, luftdruck, mintemperatur=None, maxtemperatur=None):

    """save information to csv which is later saved to database
       wahrscheinlichkeiten [0,100]
       windgeschwindigkeit [km/h]
       luftdruck  [hPa]
       temperatur [Grad Celsius]
       """

    '''Exception Handling'''

    if  type(url)!=str:
        raise  Exception('url ist kein String')

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
        raise Exception("Max und Mintemperatur können nur paarweise existieren.")



    ''' check day 
    - if day already: add to existing file

    else: same new file
    '''





    ''' save to CSV '''




save(123, 1525785827, "61231", 23.4, 80.20, 200,  10, None, )

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