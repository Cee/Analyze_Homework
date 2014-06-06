# -*- coding: cp936 -*-
__author__ = 'alex king'
from getdata import get_asin_data
import os
import string

from datetime import datetime

def max(a, b):
    if a > b:
        return a
    return b


def min(a, b):
    if a < b:
        return a
    return b


def price_line_mm(asin):
    data = get_asin_data(asin)['offer']
    price = {}
    for offer in data:
        timestamp = offer['timestamp']
        total = 0
        num = 0
        mi = 100000000000
        ma = -1
        for info in offer['info']:
            num += 1
            p = info['price']
            try:
                total += p
            except:
                print(p)
                temp = p.split('$')
                p = temp[1]
                p = p.replace(',', '')
                p = string.atof(p)
                total += p
            if p > ma:
                ma = p
            if p < mi:
                mi = p
        if price.has_key(timestamp):
            pmax = price[timestamp][0]
            pmin = price[timestamp][1]
            try:
                price[timestamp][0] = max(pmax, ma)
                price[timestamp][1] = min(pmin, mi)
                price[timestamp][2] += total
                price[timestamp][3] += num
            except:
                print(price[timestamp])
                print(ma)
                print(mi)
        else:
            price[timestamp] = [ma, mi, total, num]
    result = []
    for (k, v) in price.items():
        if v[3] != 0:
            t = ( datetime.strptime(k,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m"), v[0], v[2] / v[3], v[1])
            # print(t)
            result.append(t)
    # print('-----------------------------------')
    return result


if __name__ == '__main__':
   result = price_line_mm('B00AC8SHDW')
   print result

