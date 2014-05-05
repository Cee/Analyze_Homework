from matplotlib import pyplot as plt
from data_funcs import *
from datetime import datetime


def price_spread(asin=_ASIN_):
    productdata = get_product_data(asin)
    price_list = []
    for offer in productdata['offer']:
        for timestamp in offer['info']:
            price_list.append(timestamp['price'])
    plt.hist(price_list, histtype='bar', align='mid', color='blue', bins=5)
    plt.xlabel('price')
    plt.show()


def price_line(asin=_ASIN_):
    product_data = get_product_data(asin)
    price_list = []
    date_list = []
    for offer in product_data['offer']:
        price_list.append(offer['info'][0]['price'])
        date_list.append(datetime.strptime(offer['info'][0]['timestamp'], '%Y-%m-%d %H:%M:%S'))
    plt.plot(date_list, price_list, 'o--')
    plt.gcf().autofmt_xdate()
    plt.xlabel('date')
    plt.ylabel('price')
    plt.show()
