#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from lxml import etree


def city_url(plz: int) -> str:
    """
    Sucht auf wetter.de nach Stadt mit Postleitzahl und gibt
    Link mit URL zur aktuellen Tagesübersicht zurück

    :param plz: 5 stellige Postleitzahl deutscher Städte als Int
    :return: url mit Tagesübersicht für Stadt mit Postleitzahl
    """

    plz = str(plz)
    if len(plz) != 5:
        raise ValueError("Postcode isn't valid!")

    url = 'https://www.wetter.de/suche.html?search=' + plz.strip()
    code = urlopen(url, timeout=5)

    parser = etree.HTMLParser()
    tree = etree.parse(code, parser)
    links = tree.xpath("//a[starts-with(@id,'location-')]/@href")

    url = links[0]
    url = url.replace(".html", "/wetter-uebersicht.html")

    return url


def parse_city(url: str):
    code = urlopen(url, timeout=5)
    parser = etree.HTMLParser()
    tree = etree.parse(code, parser)


def main():
    url = city_url(14656)
    print(url)
    parse_city(url)


if __name__ == "__main__":
    main()
    # print("Not working at the moment.")
