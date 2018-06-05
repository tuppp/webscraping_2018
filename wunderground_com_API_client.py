# -*- coding: utf-8 -*-
"""
Rest Client for getting wunderground.com data
# username franz.1@campus.tu-berlin.de pw: passwort12

@author:
alexander franz 358870
daniel hartung 338991    
"""

import requests
import datetime
import os
import json
import saveCSVModel as saveModel
import time
import pdb

dateString = datetime.datetime.today().strftime('%Y-%m-%d')
localJsonSavePath = "wunderground"+dateString+".txt"
websiteName = "http://api.wunderground.com"
websiteNameShort = "wunderground"

# saves raw json response for backup purposes -> maybe use other parts later on?
def save_raw_json_response(obj):
    if not os.path.exists("raw_data"):
        os.makedirs("raw_data")

    if (os.path.exists("raw_data/" + localJsonSavePath)):
        with open("raw_data/" + localJsonSavePath, 'a') as outfile:
            json.dump(obj, outfile)
    else:
        with open("raw_data/" + localJsonSavePath, 'w') as outfile:
            json.dump(obj, outfile)


# extracts all the data out of json and saves it
def extract_and_save_data(obj, plz, file):
    if "forecast" not in obj:
        print(plz)
        return
    obj = obj["forecast"]["simpleforecast"]["forecastday"]
    for entry in obj:
        # extract data from response
        timestamp = entry["date"]["epoch"]
        mintemperatur = entry["low"]["celsius"]
        if (float(mintemperatur) <= -100 or float(mintemperatur) >= 200):
            print(plz)
            return
        if entry["high"]["celsius"] :
            maxtemperatur = entry["high"]["celsius"]
        else:
            maxtemperatur = "0"
        windgeschwindigkeit = entry["avewind"]["kph"]
        niederschlagswkeit = entry["pop"]
        if entry["qpf_allday"]["mm"]:
            niederschlagsmenge = entry["qpf_allday"]["mm"]
        else:
            niederschlagsmenge = 0
        #if niederschlagsmenge is None:
        #    niederschlagsmenge = 0
        # save relevant data to csv file
        file.save(websiteNameShort, websiteName,
                  time.time(), float(timestamp),
                  plz.rstrip(), None,
                  None, float(niederschlagswkeit),
                  float(niederschlagsmenge),
                  None, float(windgeschwindigkeit),
                  None, None,
                  float(mintemperatur),
                  float(maxtemperatur),
                  None,
                  "")

def getWunderGroundData():

    file_object = open("ZIP_Codes", "r")
    zip_codes = file_object.readlines()
    url = "http://api.wunderground.com/api/2203c5d493156b15/forecast10day/q/Germany/"
    url_appendix = ".json"
    file = saveModel.saveData()
    banned_list = ["38879", "63934", "96157", "08527", "97450", "06268", "15907", "17322", "17039", "76534",
                   "36039", "04758", "64850", "98559", "79379", "56626", "89407", "65529", "01773", "83552",
                   "63071", "95030", "24326", "48268", "91322", "72469", "73667", "29614", "51061", "25917",
                   "34560", "92224", "56823", "06366", "63679", "87437", "55494", "86476", "52385", "19258",
                   "35683", "06449", "85560", "09122", "26197", "38700", "08233", "97318", "97996", "67808",
                   "63796", "68259", "23730", "35792", "36433", "36129", "79215", "85445", "26409", "31582",
                   "12099", "47608", "66709", "23829", "27726", "99100", "27211", "15374", "79868", "86655",
                   "49191", "59889", "38116", "19399", "49624", "04916", "09496", "89568", "18119", "83088",
                   "86972", "31675", "86756", "66131", "79618", "91459", "89312", "14913", "82407", "24159",
                   "92421", "52388", "60323", "85077", "54296", "59955", "83339", "02689", "06556", "09548",

                   "06406", "51580", "01326", "39579", "66706", "15898", "77797", "96358", "94351", "26548",
                   "14641", "91781", "24398", "16775", "57080", "56410", "97074", "15837", "24229", "24803",
                   "27637", "80637", "23560", "25451", "16909", "98724", "13125", "17258", "23946", "53534",
                   "64287", "83308", "06800", "76287", "18299", "09326", "87561", "53842", "90475", "88048",
                   "25551", "01665", "18190", "96486", "38704", "01683", "54597", "72488", "90427", "82383",
                   "74592", "37186", "35099", "07427", "65207", "26721", "34626", "99817", "78464", "28199",
                   "82467", "70376", "07907", "01219", "91555", "01744", "14473", "99092", "01855", "32369",
                   "07546", "73274", "83242", "42897", "73479", "97645", "21729", "08115", "48683", "09484"
                   "54531", "77709", "91154", "07819", "99880", "18565", "96050", "97816", "95643", "17489",
                   "56355", "77933", "02977", "22335", "53229", "35435", "16278", "70794", "53819", "01994",

                   "87700", "24806", "23999", "84177", "33739", "65366", "42329", "88630", "88138", "72250",
                   "94227", "08309", "24837", "21403", "96317", "39291", "88299", "19059", "08280", "71577",
                   "59929", "07356", "94081", "95100", "35315", "18581", "91541", "87466", "91096", "84326",
                   "38899", "34630", "49594", "97896", "07957", "15328", "34414", "57612", "99974", "95500",
                   "59348", "58513", "17389", "21147", "06628", "97657", "99427", "88471", "98634", "92526",
                   "59320", "21224", "30890", "32676", "24960", "17373", "98693", "66802", "24321", "85092",
                   "78187", "98669", "63584", "47533", "16816", "84359", "27472", "55234", "82041", "83024",
                   "52525", "25856", "89188", "49716", "72555",
                   "97453", "64720", "36205", "79108", "92637", "78224", "72525", "82541", "12203", "79256",
                   "09484", "16259", "67663", "72379", "04288", "97843", "12679", "27432", "66954", "38442",
                   "82481", "92245", "93489", "14789", "59558", "26892", "07745", "79793", "75387", "74915",
                   "24790", "56865", "39615", "65594", "89558", "86609", "37269", "84453", "36381", "67433",
                   "93057", "18556", "37194", "85095", "29328", "45731", "23769", "17449", "25992", "17192",
                   "18442", "58285", "04617", "44803", "06886", "75031", "86836", "74613", "07387", "38836",
                   "24392", "64743", "17291", "54294", "38350", "55743", "86633", "86929", "16792", "17166",
                   "82216", "19309", "13405", "89160"
                   ]
    # do API call for all locations
    for index, zip_code in enumerate(zip_codes):
        if zip_code.rstrip() in banned_list:
            continue
        myResponse = requests.get(url + zip_code.rstrip() + url_appendix)

        # only write into file, when zip code is available
        if (myResponse.ok):
            obj = myResponse.json()
            save_raw_json_response(obj)
            extract_and_save_data(obj, zip_code, file)
        time.sleep(6)
def run():
    getWunderGroundData()

getWunderGroundData()