import urllib
import json
import string
# import matplotlib.pyplot as plt

from data_funcs import *
_URL_ = "http://112.124.1.3:8004/api/commodity"




def get_star(asin):
    product_data = get_product_data(asin)
    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]
    # plt.hist(star_list, color='red', align='mid', orientation='horizontal', bins=5)
    # plt.show()


def get_ASIN(category_name):
    # category_name = 'Electronics'
    specify_asin = '&field=[\'ASIN\']'
    pages = 1
    spe_url = _URL_ + '?category_name=' + category_name + specify_asin
    data = json.loads(urllib.urlopen('/'.join([spe_url])).read())
    whole_data = []
    while data != []:
        whole_data += data
        pages += 1
        spe_url = _URL_ + '?category_name=' + category_name + '&page=' + str(pages) + specify_asin
        data = json.loads(urllib.urlopen('/'.join([spe_url])).read())
    return whole_data


def get_star_data(product_asins):
    zero_star = 0
    one_star = 0
    two_star = 0
    three_star = 0
    four_star = 0
    five_star = 0

    for item_asin in product_asins:
        # print item_asin['ASIN']
        product_data_info = get_product_data(item_asin['ASIN'])['stats_info']
        average_star = string.atof(product_data_info['avg_info'])
        if (int(average_star + 0.5)) < 1:
            zero_star += 1
        elif (int(average_star + 0.5)) < 2:
            one_star += 1
        elif (int(average_star + 0.5)) < 3:
            two_star += 1
        elif (int(average_star + 0.5)) < 4:
            three_star += 1
        elif (int(average_star + 0.5)) < 5:
            four_star += 1
        else:
            five_star += 1

    print zero_star, one_star, two_star, three_star, four_star, five_star


print 'Baby Products'
get_star_data(get_ASIN('Baby Products'))
print 'Beauty'
get_star_data(get_ASIN('Beauty'))
print 'Cell Phones & Accessories'
get_star_data(get_ASIN('Cell Phones $ Accessories'))
print 'Clothing & Accessories'
get_star_data(get_ASIN('Clothing $ Accessories'))
print 'Health & Personal Care'
get_star_data(get_ASIN('Health $ Personal Care'))
print 'Home & Kitchen'
get_star_data(get_ASIN('Home $ Kitchen'))
print 'Jewelry'
get_star_data(get_ASIN('Jewelry'))
print 'Office Products'
get_star_data(get_ASIN('Office Products'))
print 'Patio, Lawn & Garden'
get_star_data(get_ASIN('Patio, Lawn $ Garden'))
print 'Pet Supplies'
get_star_data(get_ASIN('Pet Supplies'))
print 'Shoes'
get_star_data(get_ASIN('Shoes'))
print 'Sports & Outdoors'
get_star_data(get_ASIN('Sports $ Outdoors'))
print 'Tools & Home Improvement'
get_star_data(get_ASIN('Tools $ Home Improvement'))
