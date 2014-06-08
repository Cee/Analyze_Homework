#coding=utf-8

from datetime import datetime

import matplotlib.pyplot as plt

from data_funcs_local import *


_URL_ = "http://112.124.1.3:8004/api/commodity"
_ASIN_ = "B0099HX6HY"


def price_line_avg(asin):
    product_data = get_product_data(asin)
    sell_infos = []

    # remove the repeated element
    for offer in product_data['offer']:
        # print(offer)
        for sell in offer['info']:
            # print(sell)
            timestamp = (sell['timestamp'].split(' '))[0]
            link = 'Amazon.cn'
            if sell['seller'].has_key('link'):
                link = sell['seller']['link']
            onesell = [timestamp, link, sell['price']]
            # print(onesell)
            if isinarray(onesell, sell_infos):
                continue
            else:
                sell_infos.append(onesell)
    price_data = {}
    for a in sell_infos:
        if price_data.has_key(a[0]):
            price_data[a[0]]['total'] += a[2]
            price_data[a[0]]['num'] += 1
        else:
            price_data[a[0]] = {'total': a[2], 'num': 1}

            # render the chart
    time_data = []
    avg_price_data = []
    for time in price_data:
        time_data.append(datetime.strptime(time, '%Y-%m-%d'))
        avg_price_data.append(price_data[time]['total'] / price_data[time]['num'])


    plt.plot(time_data, avg_price_data, 'o--')
    plt.gcf().autofmt_xdate()  #自动调整日期显示的格式
    plt.xlabel('date')
    plt.ylabel('price')

    plt.show()


# render the price trend chart
def price_line_mm(asin):
    product_data = get_product_data(asin)
    sell_infos = []

    # remove the repeated element
    for offer in product_data['offer']:
        # print(offer)
        for sell in offer['info']:
            # print(sell)
            timestamp = (sell['timestamp'].split(' '))[0]

            # just for testing...
            # if timestamp!='2014-02-24':
            #     print(asin)
            #     print(timestamp)

            link = 'Amazon.cn'
            if sell['seller'].has_key('link'):
                link = sell['seller']['link']
            onesell = [timestamp, link, sell['price']]
            # print(onesell)
            if isinarray(onesell, sell_infos):
                continue
            else:
                sell_infos.append(onesell)
    price_data = {}
    for a in sell_infos:
        if price_data.has_key(a[0]):
            if a[2] > price_data[a[0]]['max']:
                price_data[a[0]]['max'] = a[2]
            elif a[2] < price_data[a[0]]['min']:
                price_data[a[0]]['min'] = a[2]
        else:
            price_data[a[0]] = {'max': a[2], 'min': a[2]}
            # print(price_data)
            # render the chart
    time_data = []
    max_price_data = []
    min_price_data = []
    for time in price_data:
        time_data.append(datetime.strptime(time, '%Y-%m-%d'))
        max_price_data.append(price_data[time]['max'])
        min_price_data.append(price_data[time]['min'])

    plt.plot(time_data, max_price_data, time_data, min_price_data, 'o--')
    plt.gcf().autofmt_xdate()  #自动调整日期显示的格式
    plt.xlabel('date')
    plt.ylabel('price')
    plt.show()


def isinarray(seller, array):
    isin = 0
    for onesell in array:
        if (onesell[0] == seller[0]) and (onesell[1] == seller[1]):
            isin = 1
            break
    return isin


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


'''ANALYZE PART'''
'''CHECKPOINT 1'''

if __name__ == '__main__':
    #review_hist()    #取消注释演示评论直方图的绘制
    # asin=get_asin()
    # for a in asin:
    #     # print(a['ASIN'])
    #     price_line_mm(a['ASIN'])
    price_line_avg("B000FDOW88")  #取消注释演示价格时间折线图的绘制
    #review_time()    #取消注释演示评论时间折线图的绘制
    #price_spread()
    pass