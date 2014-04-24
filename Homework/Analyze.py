__author__ = 'Cee'

import urllib
import simplejson as json
from datetime import datetime
import matplotlib.pyplot as plt

_URL_ = 'http://112.124.1.3:8004/api/commodity/'

def get_product_data():
    target_url = 'http://112.124.1.3:8004/api/commodity/B00547HWBE/'
    return json.loads(urllib.urlopen(target_url).read())

def price_spread():
    productdata = get_product_data()
    price_list = []
    for offer in productdata['offer']:
        # print(offer['timestamp'])
        for timestamp in offer['info']:
            #print(timestamp)
            # print(timestamp['price'])
            price_list.append(timestamp['price'])

    #price_list_test=[3,4,1,2,4,7,11,3,8,6,7,1,1]
    plt.hist(price_list, histtype='bar', align='mid', color='blue', bins=5)
    plt.xlabel('price')
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

def get_ASIN():
    category_name = 'Electronics>Video Game Consoles $ Accessories>Xbox 360'
    specify_asin = '&field=[\'ASIN\']'
    specify_review = '&field=[\'review\']'
    pages = 1
    spe_url = _URL_+'?category_name='+category_name+specify_asin
    data = json.loads(urllib.urlopen('/'.join([spe_url])).read())
    whole_data=[]
    # print spe_url
    # print data
    while data!=[]:
        # for i in data:
        #     print i
        #     whole_data += i\
        whole_data += data
        pages += 1
        spe_url = _URL_+'?category_name='+category_name+'&page='+str(pages)+specify_asin
        data = json.loads(urllib.urlopen('/'.join([spe_url])).read())

    return whole_data

    # product_info=[]
    # for single_product in asin_data:
    #     product_info += asin_data

def get_reviewNum(asin_data):
    product_stats = []
    review_num = {}
    product_asin = []

    for single_product in asin_data:
        item = {}
        product_asin += single_product['ASIN']
        spe_url_product = _URL_ + single_product['ASIN']
        product_data = json.loads(urllib.urlopen('/'.join([spe_url_product])).read())
        product_stats += product_data['stats_info']
        item['name'] = ((product_data['productInfo'])[0])['name']
        item['review_count'] = (product_data['stats_info'])['review_count']
        review_num[single_product['ASIN']] = item

    return review_num

def draw_comments_num_graph(source_data, asia_data):
    product_name_list = []
    product_commentNum_list = []
    commentNum_list = []
    i=1

    for asia in asia_data:
        # print source_data[asia['ASIN']]['name']
        product_name_list += [source_data[asia['ASIN']]['name']]
        product_commentNum_list += [source_data[asia['ASIN']]['review_count']]
        commentNum_list += [[source_data[asia['ASIN']]['review_count']] ]



    print product_name_list
    print product_commentNum_list

    # plt.plot(product_name_list,product_commentNum_list,'o-')
    # plt.xlabel('Product')
    # plt.ylabel('Number of comments')
    #
    # plt.xticks((1,20),product_name_list)

    # commentNum_list = [product_commentNum_list,product_name_list]
    # plt.bar(left = (0,1),height = (100,0.5),width = 1,align="center")

    # plt.hist(commentNum_list, color='grey', align='mid', bins=5, rwidth=0.5)
    #
    # plt.show()

if __name__ == '__main__':
    get_star()
    price_line()
    price_spread()
    draw_comments_num_graph(get_reviewNum(get_ASIN()), get_ASIN())
    pass