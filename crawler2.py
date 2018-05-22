
import urllib2
import re




def getParseCode(plz):
    response = urllib2.urlopen('https://www.wetterdienst.de/Deutschlandwetter/Suche/?q=' + plz)
    html = response.read()
    return html


def getFinalUrlForPlz(plz):
    code = getParseCode(plz)
    n = code.split("<tbody>")[1]
    split1 = n.split ('<td><a href="//')[2]
    return "https://" + (split1.split('"')[0]) + "Vorhersage/10-Tage-Trend/"


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def getDataForPlz(plz):

    code = urllib2.urlopen(getFinalUrlForPlz(plz))
    split1 = code.read().split('<div class="forecast_box"')

    split1.pop(0)

    nList = []
    for i in split1:

        data = {}
        split2 = i.split("Details")


        date1 =  split2[0].split('<span class="forecast_timerange">')
        date = date1[1].split('<')[0]
        data["date"] = date


        temp1 = split2[0].split('<div class="forecast_temp">')
        temp2 = temp1[1].split('</div>')

        temp =  cleanhtml(temp2[0])
        data["temperatur"] = temp


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



    print nList




getDataForPlz("10247")
