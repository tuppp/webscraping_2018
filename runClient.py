#!/home/webcrawling/miniconda3/bin/python
# -*- coding: utf-8 -*-

# from OpenWheatherMapRestClient import *
# from saveCSVModel import *


def read_plz() -> list:
    """
    Lese Datei mit Postleitzahlen ein und gebe sie als Liste zurrück

    """
    return[]


def run():
    """
    Ruft Funktionen für API-Anfragen und Crawling-Funktionen mit einzelnen PLZ auf
    --> Funktionen rufen wiederum csv Funktionen auf, um Daten zu speichern

    """

    plz_liste = read_plz()

    print("Blabb")

    """
    stadt, timestamp, temperatur, mintemperatur, maxtemperatur, windgeschwindigkeit, luftdruck, niederschlagswahrscheinlichkeit = getOpenWeatherMapData()
    pdb.set_trace()
    save(url="https://openweathermap.org/", timestamp=1526388799.745863, postleitzahl=None, stadt=stadt, temperatur=temperatur, niederschlagswahrscheinlichkeit=niederschlagswahrscheinlichkeit, windgeschwindigkeit=windgeschwindigkeit,luftdruck=luftdruck, mintemperatur=mintemperatur, maxtemperatur=maxtemperatur)
    pdb.set_trace()
    """

if __name__ == "__main__":
    run()
