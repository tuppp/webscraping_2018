from urllib.request import urlopen
from lxml import etree
from xml.etree import ElementTree
import re
import saveCSVModel
plz = ""
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


        split7 = html.split('title="Niederschlagswahrscheinlichkeit">')
        split72 = split7[1].split('</dd>')
        split72 = cleanhtml(split72 [0])
        split72 = split72.replace(" ", "")
        split72 = split72.split("|")




        date = split42[0]
        temp_max = split22[0]
        temp_min = split32[0]
        niederschlag = ""
        if(len(split72) > 1 ):
            niederschlag = split72[1]
        else:
            niederschlag = "0"

        niederschlagwkt = split72[0]
        sun_duration = split6fin [0]
        weather_state = split52[0]



        print(date)
        print (temp_min)
        print (temp_max)
        print(niederschlag)
        print(sun_duration)
        print(niederschlagwkt)
        print(weather_state)

        saveCSVModel.save(url="https://www.wetter.com",timestamp=date,postleitzahl=plz,niederschlagswahrscheinlichkeit=niederschlagwkt,mintemperatur=temp_min,maxtemperatur=temp_max)






get_16_day_prediction(get_contents('20149'))


