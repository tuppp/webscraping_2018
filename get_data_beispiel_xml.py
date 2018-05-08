#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from numpy import allclose
from os.path import exists
from socket import timeout
from os import makedirs
from lxml import etree


def loadsource(url: str):
    code = urlopen(url, timeout=5)
    return code


def parse_html_stock(code) -> (str, str, list):
    stockdata = []

    parser = etree.HTMLParser()
    tree = etree.parse(code, parser)

    time = tree.xpath("//span[@id='rt_zeit']")[0]
    timestr = time.text
    date = tree.xpath("//span[@id='rt_datum']")[0]
    date = date.text.split(".")
    datestr = "%s-%s-%s" % (date[2], date[1], date[0])

    table = tree.xpath("//table[@id='kursliste']")[0]
    zeilen = table.xpath("//tr[starts-with(@id,'spalte_')]")

    for zeile in zeilen:
        name = zeile.xpath("td[starts-with(@id,'name_')]/a")[0].text

        bid = zeile.xpath("td[starts-with(@id,'bid_')]")[0].text
        bid = float(bid.replace(",", "."))
        ask = zeile.xpath("td[starts-with(@id,'ask_')]")[0].text
        ask = float(ask.replace(",", "."))
        summe = zeile.xpath("td[starts-with(@id,'sum_')]")[0].text
        summe = int(summe.replace("\xa0", "").replace(" ", "").replace(",", "."))
        count = zeile.xpath("td[starts-with(@id,'count_')]")[0].text
        count = int(count.replace("\xa0", "").replace(" ", "").replace(",", "."))
        delta = zeile.xpath("td[starts-with(@id,'delta_')]")[0].text
        delta = float(delta.replace(",", ".").replace("%", ""))

        # TODO: Remove, debugging - Fehler liegt bei Webseite
        if allclose(bid, 0.0) or allclose(ask, 0.0):
            print(timestr, name, bid, ask, summe, count, delta, str(datetime.today()))

        stockdata.append((name, bid, ask, summe, count, delta))

    return timestr, datestr, stockdata


def get_index(url: str) -> (str, str, list):
    try:
        code = loadsource(url)
    except URLError:
        print("URLError.", str(datetime.today()))
        return "URLError", "URLError", []
    except timeout:
        print("Timeout while getting html.", str(datetime.today()))
        return "Timeout while getting html.", "Timeout while getting html.", []

    try:
        time, date, stock_data = parse_html_stock(code)
    except timeout:
        print("Timeout while parsing html.", str(datetime.today()))
        return "Timeout while parsing html.", "Timeout while parsing html.", []

    return time, date, stock_data


def get_dax() -> (str, str, list):
    dax_url = "http://www.tradegate.de/indizes.php?index=DE000A1EXRV0"
    return get_index(dax_url)


def get_mdax() -> (str, str, list):
    mdax_url = "http://www.tradegate.de/indizes.php?index=DE000A1EXRW8"
    return get_index(mdax_url)


def get_sdax() -> (str, str, list):
    sdax_url = "http://www.tradegate.de/indizes.php?index=DE000A1EXRX6"
    return get_index(sdax_url)


def get_tecdax() -> (str, str, list):
    tecdax_url = "http://www.tradegate.de/indizes.php?index=DE000A1EXRY4"
    return get_index(tecdax_url)


def write_lines(file, values):
    for i in range(len(values)):
        for j in range(5):
            file.write(values[i][j] + "; ")
        file.write(values[i][5] + "\n")
    file.write("\n\n")
    return


def print_dax_tecdax_as_csv(time_dax, dax, time_tec, tec):
    pfad = "../databases"
    if not exists(pfad):
        makedirs(pfad)

    filename = "../databases/tecdax_dax_" + time_dax.replace(":", "_") + ".csv"
    file = open(filename, "w")

    file.write("DAX Werte um " + time_dax + " Uhr\n")
    write_lines(file, dax)

    file.write("TECDAX Werte um " + time_tec + " Uhr\n")
    write_lines(file, tec)

    file.close()
    return
