'''
is script is started with runClient.bash due to anaconda env needed for certain imports
#!/home/webcrawling/miniconda3/bin/python
# -*- coding: utf-8 -*-
'''

import openweathermap_org_API_client
import wetterdienst_de
import accuweather_com_API_client
import wetter_com_crawler
import datetime

def run():

    print("Wetterdienst:" + str(datetime.datetime.now()))
    wetterdienst_de.start()

    print("WEtter.com" + str(datetime.datetime.now()))
    wetter_com_crawler.start()


    print("Openweathermap" + str(datetime.datetime.now()))
    openweathermap_org_API_client.run()

    print("Acu:" + str(datetime.datetime.now()))
    accuweather_com_API_client.run()




if __name__ == "__main__":
    run()
