from datetime import datetime
import time
import re

from urllib.request import urlopen

import saveCSVModel

counter = 0


def increment_counter():
    global counter
    counter += 1


def loadsource(url: str):
    code = urlopen(url, timeout=5)
    return code


def get_contents(plz):
    string_1 = 'https://www.wetter.com/suche/?q='
    url_final = string_1 + plz
    return loadsource(url_final), plz


def get_16_day_prediction(code, plz):
    c1 = code.read()
    split_first = c1.decode().split('data-label="VHSTabZeitraum_16"')

    try:
        split_first_2 = split_first[1]
        dirty_html = split_first_2.split('href="')
        dirty_html = dirty_html[1]
        clean_html = dirty_html.split('"')[0]
        get_all_predictions(clean_html, plz)
    except Exception:
        increment_counter()
        print("PLZ nicht erkannt")


def string_to_date(string_s):
    string_s = string_s.split(" ")[1]
    timestr = '2018-' + string_s.split(".")[1] + '-' + string_s.split(".")[0]
    return time.mktime(datetime.strptime(timestr, '%Y-%m-%d').timetuple())


def string_to_float(string_s):
    value = re.findall(r'\d+', string_s)
    if len(value) == 0:
        return float(0)
    else:
        return float(value[0])


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_all_predictions(url, plz):
    code = loadsource(url)
    new_code = code.read()
    plz = plz.replace("\n", "")

    split1 = new_code.decode().split(' class="weather-grid-item"')

    split1.pop(0)
    count = 0
    for html in split1:
        count = count + 1

        split2 = html.split('<span class="temp-max">')
        split22 = split2[1].split('</span>')
        split3 = html.split('<span class="temp-min">')
        split32 = split3[1].split('</span>')

        split4 = html.split('date">')
        split42 = split4[1].split('<')

        split6 = html.split('<span class="icon-sun_hours icon--small mr--" title="Sonnenstunden" />')
        split62 = split6[1].split('</dd>')
        split63 = split62[0].split("<dd>")
        split6fin = split63[1]

        split7 = html.split('title="Niederschlagswahrscheinlichkeit">')
        split72 = split7[1].split('</dd>')
        split72 = cleanhtml(split72[0])
        split72 = split72.replace(" ", "")
        split72 = split72.split("|")

        date = split42[0]
        date = string_to_date(date)
        temp_max = string_to_float(split22[0])
        temp_min = string_to_float(split32[0])

        if len(split72) > 1:
            niederschlag = split72[1]
        else:
            niederschlag = "0"

        niederschlag = string_to_float(niederschlag)
        niederschlagwkt = string_to_float(split72[0])
        sun_duration = string_to_float(split6fin)

        c = saveCSVModel.SaveData()

        c.save(websitename="wetter_com", url="https://www.wetter.com", timestamp=time.time(), timestamppred=date,
               postleitzahl=plz, niederschlagsmenge=niederschlag, sonnenstunden=sun_duration,
               niederschlagswahrscheinlichkeit=niederschlagwkt, mintemperatur=temp_min, maxtemperatur=temp_max)


def read_plz_data():
    plz_list = []
    fp = open("ZIP_Codes")
    for i, line in enumerate(fp):
        plz_list.append(str(line))

    return plz_list


def predictions_plz(ziplist):
    for i in ziplist:
        get_16_day_prediction(*get_contents(i))


def start():
    predictions_plz(read_plz_data())


if __name__ == "__main__":
    predictions_plz(read_plz_data())
