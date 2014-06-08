__author__ = 'Xc'

from datetime import datetime

from data_funcs_local import *

import matplotlib.pyplot as plt

import oneyear


def star(cate_name='Beauty>Hair Care>Shampoos'):
    cate_name = cate_name.replace('&', '$')
    stars = [0, 0, 0, 0, 0]
    for asin in get_asin_in_category(cate_name):
        data = get_product_data(asin)
        for i in range(5):
            try:
                stars[i] += int(data['stats_info']['star_info']['%d' % (i + 1)])
            except Exception:
            # stars[i] += int(data['stats_info']['star_info'][i])
                print '----------------------------------------------------------------'
                print data
                print '----------------------------------------------------------------'

    stars = (stars[0], stars[1], stars[2], stars[3], stars[4])
    return stars


def prize(cate_name='Beauty>Hair Care>Shampoos'):
    cate_name = cate_name.replace('&', '$')
    prize_record = []
    for asin in get_asin_in_category(cate_name):
        prizes = oneyear.prize(asin)
        prize_record.append(prizes)

    # print prize_record
    prizes_d = [[record[i][1]for record in prize_record if record[i][1] is not None ] for i in range(12)]
    # print prizes_d
    prizes_d = [( prize_record[0][i][0] ,(sum(prizes_d[i]) / len(prizes_d[i])) if len(prizes_d[i]) >0 else None  ) for i in range(12)]
    # print prizes_d
    return  prizes_d


def comment(cate_name='Beauty>Hair Care>Shampoos'):
    cate_name = cate_name.replace('&', '$')
    comment_record = []
    for asin in get_asin_in_category(cate_name):
        comments = oneyear.comment(asin)
        comment_record.append(comments)
    comment_d = [[record[i][1]for record in comment_record if record[i][1] is not None ] for i in range(12)]
    comment_d = [( comment_record[0][i][0] ,sum(comment_d[i])) for i in range(12)]
    return comment_d



if __name__ == '__main__':
    for one in comment('Electronics>Cell Phones & Accessories>Mobile Broadband'):
        print one