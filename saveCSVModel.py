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

    if niederschlagswahrscheinlichkeit is not None:
        if type(niederschlagswahrscheinlichkeit)!=float:
            raise Exception('niederschlagswahrscheinlichkeit kein float')

        if niederschlagswahrscheinlichkeit < 0 or niederschlagswahrscheinlichkeit > 1:
            raise Exception('niederschlagswahrscheinlichkeit nicht zwischen 0 und 1')

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