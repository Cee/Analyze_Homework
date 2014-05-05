__author__ = 'Xc'

from data_funcs import *

_ASIN_ = "B0099HX6HY"
import matplotlib.pyplot as plt

'''CHECKPOINT 3'''


def get_star(asin=_ASIN_):
    product_data = get_product_data(asin)
    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]
    print len(product_data['review'])
    count_list = [0, 0, 0, 0, 0]
    for each in star_list:
        count_list[(int)(each) - 1] += 1
    print count_list
    plt.hist(star_list, color='red', align='mid', orientation='horizontal', bins=5)
    plt.show()
