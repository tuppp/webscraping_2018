#!/home/webcrawling/miniconda3/envs/mkp/bin/python
# -*- coding: utf-8 -*-

"""
anaconda env needed for certain imports
"""

import os
import sys
import datetime

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
import openweathermap_org_API_client
import wetterdienst_de
import accuweather_com_API_client
import wetter_com_crawler


def run():
    print("Wetterdienst:" + str(datetime.datetime.now()))
    wetterdienst_de.start()

    print("Wetter.com" + str(datetime.datetime.now()))
    wetter_com_crawler.start()

    print("Openweathermap" + str(datetime.datetime.now()))
    openweathermap_org_API_client.run()

    print("Acu:" + str(datetime.datetime.now()))
    accuweather_com_API_client.run()


if __name__ == "__main__":
    run()
