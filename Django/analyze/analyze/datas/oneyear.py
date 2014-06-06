__author__ = 'Xc'

from datetime import datetime

from data_funcs_local import *

import matplotlib.pyplot as plt

_ASIN_ = 'B00AC8SHDW'

special_date_list = [
    '2013.07.01', '2013.08.01', '2013.09.01',
    '2013.10.01', '2013.11.01', '2013.12.01',
    '2014.01.01', '2014.02.01', '2014.03.01',
    '2014.04.01', '2014.05.01', '2014.06.01',
]
special_date_list = [datetime.strptime(i, '%Y.%m.%d') for i in special_date_list]


def special_date_prize(asin=_ASIN_):
    pdata = get_product_data(asin)
    offerdata = pdata['offer']
    offerdata = sorted(offerdata, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))

    pricelist = []
    for special_date in special_date_list:
        flag = True
        for i in range(len(offerdata) - 1):
            a_offer = offerdata[i]
            if (special_date >= datetime.strptime(offerdata[i]['timestamp'], '%Y-%m-%d %H:%M:%S')) and \
                    (special_date < datetime.strptime(offerdata[i + 1]['timestamp'], '%Y-%m-%d %H:%M:%S')):
                if len(a_offer['info']) >= 1:
                    pricelist.append(float(a_offer['info'][0]['price']))
                else:
                    pricelist.append(None)
                flag = False
            break
        if flag:
            pricelist.append(None)

    print len(special_date_list)
    print len(pricelist)

    # plt.plot(special_date_list, pricelist, 'ro')
    # plt.gcf().autofmt_xdate()
    # plt.xlabel('Time')
    # plt.ylabel('Price')
    # plt.show()


def special_date_review(asin=_ASIN_):
    pdata = get_product_data(asin)
    reviewdata = pdata['review']
    reviewdata.sort(key=lambda x: datetime.strptime(x['publishTime'], '%Y-%m-%d %H:%M:%S'))

    count_list = []
    for special_date in special_date_list:
        count = 0;
        for a_review in reviewdata:
            if special_date.strftime('%Y%m%d') == datetime.strptime(a_review['publishTime'],
                                                                    '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d'):
                #do some thing
                count += 1
        count_list.append(count)
    plt.plot(special_date_list, count_list, 'ro-')
    plt.gcf().autofmt_xdate()
    plt.xlabel('Time')
    plt.ylabel('Review Count')
    plt.show()


def prize(asin=_ASIN_):
    pdata = get_product_data(asin)
    offerdata = pdata['offer']
    offerdata = sorted(offerdata, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))

    pricelist = []
    for special_date in special_date_list:
        flag = True
        for i in range(len(offerdata) - 1):
            a_offer = offerdata[i]
            if (special_date >= datetime.strptime(offerdata[i]['timestamp'], '%Y-%m-%d %H:%M:%S')) and \
                    (special_date < datetime.strptime(offerdata[i + 1]['timestamp'], '%Y-%m-%d %H:%M:%S')):
                if len(a_offer['info']) >= 1:
                    pricelist.append(float(a_offer['info'][0]['price']))
                else:
                    pricelist.append(None)
                flag = False
            break
        if flag:
            pricelist.append(None)
    return [(x.strftime('%Y-%m-%d'), 0 if y is None else float(y)) for x, y in zip(special_date_list, pricelist)]


def comment(asin=_ASIN_):
    pdata = get_product_data(asin)
    reviewdata = pdata['review']
    reviewdata.sort(key=lambda x: datetime.strptime(x['publishTime'], '%Y-%m-%d %H:%M:%S'))

    count_list = []
    for special_date in special_date_list:
        count = 0;
        for a_review in reviewdata:
            if special_date.strftime('%Y%m%d') == datetime.strptime(a_review['publishTime'],
                                                                    '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d'):
                #do some thing
                count += 1
        count_list.append(count)
    return [(x.strftime('%Y-%m'), int(y)) for x, y in zip(special_date_list, count_list)]

special_date_listc = special_date_list[::2]


def isinarray(seller, array):
    isin = 0
    for onesell in array:
        if (onesell[0] == seller[0]) and (onesell[1] == seller[1]):
            isin = 1
            break
    return isin

if __name__ == '__main__':
    for x, y in avg('B000FDOW88'):
        print x, y