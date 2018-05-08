from urllib import urlopen
import re

def get_all_bundeslaender():
    url = 'https://www.wetter.de/deutschland'
    site = urlopen(url)
    site_read = site.read()
    first_split = site_read.split('<ul class="large-block-grid-3 small-block-grid-2 unstyled">')
    dirty_array = first_split [1]

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', dirty_array)

    return urls

def get_all_locations_bl(url):
    s = '<div class="large-8 small-12 alpha omega">'
    s_string = '<ul class="large-block-grid-3 small-block-grid-2 unstyled">'
    site = urlopen(url)
    site_read = site.read()
    first_split = site_read.split(s_string)
    dirty_html = first_split [1]
    clean_html = dirty_html.split(s)
    use_html =  clean_html [0]
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',use_html)
    return urls
def get_measurements(url):
    s_string = '$AC.loadConfig({"autoDetection"'
    s_string_2 = ',"ivw":"\/wetterde\/deutschland\/'
    s_string_3 = '"keys":'
    site = urlopen(url)
    site_read = site.read()
    first_split = site_read.split(s_string)
    dirty_html = first_split [1]
    clean_html = dirty_html.split(s_string_2)
    use_html = clean_html [0]
    measurements = (use_html.split(s_string_3)) [1]
    print(measurements)
    return measurements


def get_all_measurements():
    ger_measurements = []
    bundesland_urls = get_all_bundeslaender()
    for bundesland in bundesland_urls:
        local_list = get_all_locations_bl(bundesland)
        for local in local_list:
            ger_measurements.append(get_measurements(local))

    return ger_measurements



def put_list_into_file(all_msm):
    f = open('measurement_log', 'a')
    f.write(all_msm)
    f.close()

#get_all_bundeslaender()
#get_all_locations_bl('https://www.wetter.de/deutschland/wetter-karte-baden-wuerttemberg-c49p8.html')
#get_measurements("")
print get_all_measurements()
