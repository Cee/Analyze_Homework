import urllib
import json

import matplotlib.pyplot as plt
from datetime import datetime

'''PUBLIC VARIBLES'''
_URL_ = "http://112.124.1.3:8004/api/commodity"
_ASIN_ = "B0099HX6HY"


def get_asin():
    category_name = 'Electronics>Video Game Consoles $ Accessories>Xbox 360'
    specify_asin = '&field=[\'ASIN\']'
    specify_review = '&field=[\'review\']'
    pages = 1
    spe_url = _URL_ + '?category_name=' + category_name + specify_asin
    data = json.loads(urllib.urlopen('/'.join([spe_url])).read())
    whole_data = []
    while data:
        # for i in data:
        #     print i
        #     whole_data += i\
        whole_data += data
        pages += 1
        spe_url = _URL_ + '?category_name=' + category_name + '&page=' + str(pages) + specify_asin
        data = json.loads(urllib.urlopen('/'.join([spe_url])).read())
    # print whole_data
    return whole_data


def get_review_num(asin_data):
    """CHECKPOINT 2"""

    product_stats = []
    review_num = {}
    product_asin = []

    for single_product in asin_data:
        item = {}
        product_asin += single_product['ASIN']
        spe_url_product = _URL_ + single_product['ASIN']
        product_data = get_product_data(single_product['ASIN'])
        product_stats += product_data['stats_info']
        item['name'] = ((product_data['productInfo'])[0])['name']
        item['review_count'] = (product_data['stats_info'])['review_count']
        review_num[single_product['ASIN']] = item

    return review_num


from comment import *
from price import *
from price_line import *
from special_date import *
from star import *

if __name__ == '__main__':
    #from price.py
    price_line()
    price_spread()

    #from coment.py
    draw_comments_num_graph(get_review_num(get_asin()), get_asin())

    #from price_line.py
    price_line_mm("B002VBWIP6")
    price_line_avg("B0089KDCIU")

    #from special_date.py
    special_date_review("B00547HWBE")
    special_date_prize("B00547HWBE")

    #from star.py
    get_star('B00F6NB8WU')
    pass