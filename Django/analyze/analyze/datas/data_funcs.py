__author__ = 'Xc'
_URL_ = "http://112.124.1.3:8004/api/commodity"
_ASIN_ =  "B0099HX6HY"
import json
import urllib


def get_all_category():
    url = _URL_
    jdata = json.load(urllib.urlopen(url))
    return [data['name'] for data in jdata]


def get_product_data(product_asin, field=None):
    if not field:
        url = "http://112.124.1.3:8004/api/commodity/" + product_asin
    else:
        url = r"http://112.124.1.3:8004/api/commodity/%s/?field=['%s']" % (product_asin, field)

    while True:
        try:
            jdata = json.load(urllib.urlopen(url))
            return jdata
        except Exception:
            pass


def get_asin_in_category(category_name):
    jdata = []
    i = 1
    while True:
        url = _URL_ + "?category_name=" + category_name + "&page=%d&field=['ASIN']" % i
        # print url
        data = json.load(urllib.urlopen(url))
        data = [one_data['ASIN'] for one_data in data]
        if data:
            jdata.extend(data)
            i += 1
        else:
            break
    return jdata
