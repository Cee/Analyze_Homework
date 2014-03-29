#-*- coding:utf-8-*-

#######################
# 根据数据简单绘制一些统计图表
#
# Author: Cheng@NJU
#######################

import urllib
import simplejson as json

from datetime import datetime
import matplotlib.pyplot as plt

#######################################################
#根据 http://112.124.1.3:8004/api/commodity/B00547HWBE/
# 的信息来进行Demo演示
#######################################################

def get_product_data():
    '''获取Demo的商品信息'''
    target_url = 'http://112.124.1.3:8004/api/commodity/B00547HWBE/'
    return json.loads(urllib.urlopen(target_url).read())

def review_hist():
    '''根据评论绘制出评论打分的直方图'''    
    product_data = get_product_data()
    
    star_list = [float(single_review['star'].split()[0]) \
                 for single_review in product_data['review']]
    
    plt.hist(star_list, color ='grey', align = 'mid', bins = 5, rwidth = 0.5)
    
    plt.show()


def price_line():
    '''根据价格绘制出价格走向的折线图'''
    product_data = get_product_data()
    
    price_list=[]
    date_list=[]
    
    #这里只是取每个阶段的第一个价格，实际上可以绘制所有价格的曲线
    for offer in product_data['offer']:
        price_list.append(offer['info'][0]['price'])
        date_list.append(datetime.strptime(offer['info'][0]['timestamp'], 
                                           '%Y-%m-%d %H:%M:%S'))
    
    
    plt.plot(date_list, price_list, 'o--')
    plt.gcf().autofmt_xdate()   #自动调整日期显示的格式
    plt.xlabel('日期')
    plt.ylabel('价格')
    
    plt.show()

def incre_list(origin_list):
    '''数组元素递加'''
    return [sum(origin_list[0: idx]) for idx,ele in enumerate(origin_list)]

def review_time():
    '''根据评论绘制时间增量图'''
    product_data = get_product_data()
    
    time_list = []
    
    for review in product_data['review']:
        time_list.append(datetime.strptime(review['publishTime'],
                                           '%Y-%m-%d %H:%M:%S'))
    time_list = list(set(time_list))    
    review_count_dict = {}
    
    for single_date in time_list[::-1]:
        review_count_dict[int(single_date.strftime('%Y%m'))] = review_count_dict[int(single_date.strftime('%Y%m'))] + 1 \
            if review_count_dict.has_key(int(single_date.strftime('%Y%m'))) else 1
    
    review_count_list = sorted(review_count_dict.iteritems(), key=lambda x:x[0])
    
    count_data = incre_list(map(lambda x:x[1], review_count_list))
    date_data = map(lambda x:datetime.strptime(str(x[0]), '%Y%m'), review_count_list)
    
    plt.plot(date_data, count_data, 'ro-')
    plt.gcf().autofmt_xdate()
    plt.xlabel('Time')
    plt.ylabel('Review Count')
    plt.ylim([0,max(count_data)])
    
    plt.show()

if __name__ == '__main__':
    #review_hist()    #取消注释演示评论直方图的绘制
    #price_line()     #取消注释演示价格时间折线图的绘制
    #review_time()    #取消注释演示评论时间折线图的绘制
    pass