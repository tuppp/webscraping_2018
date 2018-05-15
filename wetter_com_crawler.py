from urllib.request import urlopen
from lxml import etree
from xml.etree import ElementTree


string_1 = 'https://www.wetter.com/suche/?q=10115'

def loadsource(url: str):
    code = urlopen(url, timeout=5)
    return code

def get_contents(plz):
    string_1 = 'https://www.wetter.com/suche/?q='
    url_final = string_1 + plz
    return loadsource(url_final)

def parse_html_stock(code):
    stockdata = []

    parser = etree.HTMLParser()
    tree = etree.parse(code, parser)

    time = tree.xpath("//span[@class='text--h-size-6']") [0]
    time.text
parse_html_stock(get_contents('20149'))