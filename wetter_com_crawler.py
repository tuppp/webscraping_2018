from urllib.request import urlopen
from lxml import etree
from xml.etree import ElementTree
import re
import saveCSVModel
import time
import datetime
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
plz = "10367"
string_1 = 'https://www.wetter.com/suche/?q=10115'

def loadsource(url: str):
    code = urlopen(url, timeout=5)
    return code

def get_contents(plz):
    string_1 = 'https://www.wetter.com/suche/?q='
    url_final = string_1 + plz
    return loadsource(url_final)

def get_16_day_prediction(code):
    c1 = code.read()
    split_first = c1.decode().split('data-label="VHSTabZeitraum_16"')
    split_first_2 = split_first [1]
    dirty_html = split_first_2.split('href="')
    dirty_html = dirty_html [1]
    clean_html = dirty_html.split('"') [0]
    print(clean_html)
    get_all_predictions(clean_html)


def string_to_date(string_s):
    war_start = '2011-01-03'
    string_s = string_s.split(" ") [1]
    return time.mktime(datetime.strptime('2018-' + string_s.split(".")[1] + '-' + string_s.split(".")[0], '%Y-%m-%d').timetuple())
def string_to_float(string_s):
    value = re.findall(r'\d+', string_s)
    if len(value) == 0 :
        return float(0)
    else:
        return float(value[0])



def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
def get_all_predictions(url):
    code = loadsource(url)
    new_code = code.read()

    split1 = new_code.decode().split(' class="weather-grid-item"')


    split1.pop(0)
    count = 0
    for html in split1:
        count = count +1
        print(count)


        split2 = html.split('<span class="temp-max">')
        split22 = split2[1].split('</span>')
        split3 = html.split('<span class="temp-min">')
        split32 = split3[1].split('</span>')

        split4 = html.split('date">')
        split42 = split4[1].split('<')

        split5 = html.split('<div class="weather-state">')
        split52 = split5[1].split('<')

        split6 = html.split('<span class="icon-sun_hours icon--small mr--" title="Sonnenstunden" />')
        split62 = split6[1].split('</dd>')
        split63 = split62[0].split("<dd>")
        split6fin = split63[1]
        print(split6fin)


        split7 = html.split('title="Niederschlagswahrscheinlichkeit">')
        split72 = split7[1].split('</dd>')
        split72 = cleanhtml(split72 [0])
        split72 = split72.replace(" ", "")
        split72 = split72.split("|")




        date = split42[0]
        date = string_to_date(date)
        temp_max = string_to_float(split22[0])
        temp_min = string_to_float(split32[0])
        print(type(temp_min))
        niederschlag = ""
        if(len(split72) > 1 ):
            niederschlag = split72[1]
        else:
            niederschlag = "0"
        niederschlag = string_to_float(niederschlag)
        niederschlagwkt = string_to_float(split72[0])
        sun_duration = string_to_float(split6fin)
        weather_state = string_to_float(split52[0])



        c = saveCSVModel.saveData()

        c.save(websitename="wetter_com",url="https://www.wetter.com",timestamp=time.time(),timestamppred=date,postleitzahl=plz,niederschlagsmenge=niederschlag,sonnenstunden=sun_duration,niederschlagswahrscheinlichkeit=niederschlagwkt,mintemperatur=temp_min,maxtemperatur=temp_max)






get_16_day_prediction(get_contents('20149'))


