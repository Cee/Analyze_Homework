__author__ = 'Cee'

import urllib
import simplejson as json
from datetime import datetime
import matplotlib.pyplot as plt

def get_product_data():
    target_url = 'http://112.124.1.3:8004/api/commodity/B00547HWBE/'
    return json.loads(urllib.urlopen(target_url).read())

def price_spread():
    productdata = get_product_data()
    price_list = []
    for offer in productdata['offer']:
        print(offer['info'][0]['price'])
        price_list.append(offer['info'][0]['price'])
    # price_list_test=[3,4,1,2,4,7,11,3,8,6,7,1,1]
    plt.hist(price_list, histtype='bar', align='mid', color='blue', bins=5)
    plt.show()

def price_line():
    product_data = get_product_data()

    price_list=[]
    date_list=[]

    for offer in product_data['offer']:
        print(offer['info'][0]['price'])
        price_list.append(offer['info'][0]['price'])
        print(offer['info'][0]['timestamp'])
        date_list.append(datetime.strptime(offer['info'][0]['timestamp'],
                                           '%Y-%m-%d %H:%M:%S'))

    print('end')
    plt.plot(date_list, price_list, 'o--')
    plt.gcf().autofmt_xdate()
    plt.xlabel('date')
    plt.ylabel('price')

    plt.show()

def get_star():
    product_data = get_product_data()

    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]

    plt.hist(star_list, color='red', align='mid', orientation='horizontal', bins=5)

    plt.show()

if __name__ == '__main__':
    get_star()
    #price_line()
    price_spread()
    pass