# -*- coding: utf-8 -*-
"""
Filter geodata for our zipcodes - just for Frontend

@author:
alexander franz 358870
daniel hartung 338991
"""

import json


def ger_zip_to_our_zip():

    # read all geo data with corresponding zip codes
    file_object = open("postleitzahlen.geojson", "r", encoding="utf-8-sig")
    obj = file_object.read()
    big_json = json.loads(obj)

    # read our zip codes
    file_object = open("ZIP_Codes", "r")
    our_zip_codes = file_object.readlines()

    new_list = []
    # filter all zip codes we don´t need
    for entry in big_json["features"]:
        found_zipcode = ''
        for zip_code in our_zip_codes:
            if entry["properties"]["postcode"] == zip_code.rstrip():
                found_zipcode = 'X'
        if found_zipcode == 'X':
            new_list.append(entry)
            # print(entry["properties"]["postcode"])

    sorted_new_list = sorted(new_list, key=lambda x: x["properties"]["postcode"])
    big_json["features"] = sorted_new_list

    # open new target file for desired geo data and save it
    target_file = open("zip_code_plus_geo_data.geojson", 'a', encoding="utf-8-sig")
    json.dump(big_json, target_file, ensure_ascii=False)
    target_file.close()


if __name__ == "__main__":
    ger_zip_to_our_zip()
