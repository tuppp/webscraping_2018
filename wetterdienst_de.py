
from urllib.request import urlopen
import re
import time
import datetime
import pandas as pd
from dateutil.parser import parse
import saveCSVModel






#######AUFRUF : getDataForPlz("10247")





def bereinigen(str):

    nstr = str.replace('\n', "")
    nstr = nstr.replace('\r', "")
    nstr = nstr.replace('*', "°C")
    nstr = nstr.replace('°C', "")
    return nstr

def getParseCode(plz):
    plz = plz.replace('\n', '')
    response = urlopen('https://www.wetterdienst.de/Deutschlandwetter/Suche/?q=' + plz + '&where=DE')

    html = response.read()

    return html


def getFinalUrlForPlz(plz):
    code = getParseCode(plz)
    n = code.decode().split("<tbody>")[1]

    split1 = n.split('<td><a href="//')[1]

    return "https://" + (split1.split('"')[0]) + "Vorhersage/10-Tage-Trend/"


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def getDataForPlz(plz):
    url = getFinalUrlForPlz(plz)
    code = urlopen(url)
    split1 = code.read().decode().split('<div class="forecast_box"')

    split1.pop(0)

    nList = []
    for i in split1:

        try:
            data = {}
            split2 = i.split("Details")
            data["url"] = url

            date1 =  split2[0].split('<span class="forecast_timerange">')
            date = date1[1].split('<')[0]
            data["date"] = date


            temp1 = split2[0].split('<div class="forecast_temp">')
            temp2 = temp1[1].split('</div>')

            temp = cleanhtml(temp2[0])
            data["temperatur"] = bereinigen(temp)

            tempsplit = data["temperatur"].split("/")
            data["mintemp"] = float(tempsplit[0])
            data["maxtemp"] = float(tempsplit[1])



            niederschlag1 = split2[0].split('<div class="forecast_prec" style="padding-top: 15px;">')
            niederschlag2 = niederschlag1[1].split('</span>')

            niederschlag3 = cleanhtml(niederschlag2[0])


            if "umbrella" in niederschlag3:
                niederschlag3 = niederschlag3.split(">")[1]

            data["niederschlag"] = niederschlag3

            niederschlagswahrscheinlichkeit1 = split2[0].split('Niederschlag: <strong>')

            niederschlagswahrscheinlichkeit2 = niederschlagswahrscheinlichkeit1[1].split('<')[0]

            data["niederschlagswahrscheinlichkeit"] = niederschlagswahrscheinlichkeit2

            nList.append(data)
        except:
            print("WETTERDIENST PLZ FEHLGESCHLAGEN: " + plz)



    c = saveCSVModel.saveData()
    for x in nList:

        c.save(url=x["url"], timestamp = time.time(), timestamppred = datetime.datetime.strptime(x["date"], "%d.%m.%Y").timestamp(),postleitzahl=plz, stadt="", mintemperatur= x["mintemp"], maxtemperatur= x["maxtemp"], websitename="WETTERDIENST")






def start():
    try:
        with open('ZIP_Codes') as f:
           for line in f:
            line = line.replace("\n", "")
            getDataForPlz(line)
    except:
        print("ERROR WETTERDIENST")
#start()
