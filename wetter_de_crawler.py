#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from socket import timeout
from lxml import etree


def get_bundeslaender():
    url = 'https://www.wetter.de/deutschland'
    code = urlopen(url, timeout=5)

    parser = etree.HTMLParser()
    tree = etree.parse(code, parser)

    links = tree.xpath("//a[@id='menu-map-country-deutschland']")[0]
    links = links.xpath("//a[starts-with(@id,'menu-province-')]/@href")

    return links


def main():
    try:
        pass
    except URLError:
        print("URLError.", str(datetime.today()))
        exit(1)
    except timeout:
        print("Timeout while getting html.", str(datetime.today()))
        exit(1)


if __name__ == "__main__":
    # main()
    print("Not working at the moment.")
