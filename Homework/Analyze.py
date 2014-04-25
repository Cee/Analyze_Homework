import urllib
import simplejson as json
from datetime import datetime
import matplotlib.pyplot as plt

_URL_ = "http://112.124.1.3:8004/api/commodity/"

def get_product_info(product_asin):
    url = _URL_ + product_asin + "?field=['productInfo']"
    jdata = json.load(urllib.urlopen(url))
    return jdata

def get_product_data(product_asin):
    url = _URL_ + product_asin
    jdata = json.load(urllib.urlopen(url))
    return jdata

def get_all_category():
    url = _URL_
    jdata = json.load(urllib.urlopen(url))
    return [data['name'] for data in jdata]


def price_spread():
    productdata = get_product_data('B00547HWBE')
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
    product_data = get_product_data('B00547HWBE')

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
    product_data = get_product_data('B00547HWBE')

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

def get_asin_in_category(category_name):
    jdata = []
    i = 1
    while True:
        url = "http://112.124.1.3:8004/api/commodity?category_name=" + category_name + "&page=%d&field=['ASIN']" % i
        # print url
        data = json.load(urllib.urlopen(url))
        data = [one_data['ASIN'] for one_data in data]
        if (len(data) >= 1):
            jdata.extend(data)
            i += 1
        else:
            break
    return jdata



def compare(special_time, time1, time2):
    return True

    time2 = datetime.strptime(time2)
    time2 = time2.strftime("%m.%d")
    if (special_time >= time1) & (special_time < time2):
        return True
    else:
        return False


special_date_list = [
    '2013.01.01',
    '2013.02.14',
    '2013.03.14',
    '2013.04.01',
    '2013.05.01',
    '2013.06.01',
    '2013.11.01',
    '2013.12.24',
    '2013.12.25',
    '2014.01.01',
    '2014.02.14',
    '2014.03.14',
    '2014.04.01',
    '2014.05.01',
    '2014.06.01',
    '2014.11.01',
    '2014.12.24',
    '2014.12.25',
]
special_date_list = [datetime.strptime(i, '%Y.%m.%d') for i in special_date_list]


def prize(asin='B00547HWBE'):
    pdata = get_product_data(asin)
    offerdata = pdata['offer']  #   all data in offer a list
    offerdata = sorted(offerdata, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))

    pricelist = []
    for special_date in special_date_list:
        flag = True
        for i in range(len(offerdata) - 1):
            a_offer = offerdata[i]
            if ( special_date >= datetime.strptime(offerdata[i]['timestamp'], '%Y-%m-%d %H:%M:%S') ) & (
                        special_date < datetime.strptime(offerdata[i + 1]['timestamp'], '%Y-%m-%d %H:%M:%S') ):
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

    plt.plot(special_date_list, pricelist, 'ro')
    plt.gcf().autofmt_xdate()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()


def review(asin='B0099HX6HY'):
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

if __name__ == '__main__':
    get_star()
    # price_line()
    price_spread()
    draw_comments_num_graph(get_reviewNum(get_ASIN()), get_ASIN())
    prize()
    review()
    pass