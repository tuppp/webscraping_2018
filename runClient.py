'''
is script is started with runClient.bash due to anaconda env needed for certain imports
#!/home/webcrawling/miniconda3/bin/python
# -*- coding: utf-8 -*-
'''

import openweathermap_org_API_client
import wetterdienst_de
import accuweather_com_API_client
import wetter_com_crawler

def run():
    ''' run scripts like this. handle plz internally. sorry daniel for changes here.. '''
    accuweather_com_API_client.run()
    wetterdienst_de.start()
    openweathermap_org_API_client.run()
    wetter_com_crawler.start()




if __name__ == "__main__":
    run()
