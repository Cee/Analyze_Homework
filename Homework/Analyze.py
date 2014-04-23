__author__ = 'Cee'

import urllib
import simplejson as json

import matplotlib.pyplot as plt

def get_product_data():
    target_url = 'http://112.124.1.3:8004/api/commodity/B00547HWBE/'
    return json.loads(urllib.urlopen(target_url).read())

def review_hist():
    product_data = get_product_data()

    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]

    plt.hist(star_list, color ='blue', align = 'mid', bins = 5, rwidth = 1)

    plt.show()

if __name__ == '__main__':
    review_hist()
    pass