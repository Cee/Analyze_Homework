__author__ = 'Xc'

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect

from datas.data_funcs_local import *


import datas.keyowrd_solu2 as key_ana
import datas.oneyear
import datas.minmax

jump_to_index_hmtl = '<html><script>location.assign("/index");</script></html>'


def index_html(request, no_use):
    return render_to_response("index.html")


def jump_index(request):
    return HttpResponse(jump_to_index_hmtl)


def category(request):
    pass


def product_info(request):
    if 'ASIN' in request.GET:
        asin = request.GET['ASIN']
        if asin != "":
            data = get_product_data(asin)
            if data is None:
                raise Http404
            product_name = data['productInfo'][0]['name']

            one_stars_number = int(data['stats_info']['star_info']['1'])
            two_stars_number = int(data['stats_info']['star_info']['2'])
            three_stars_number = int(data['stats_info']['star_info']['3'])
            four_stars_number = int(data['stats_info']['star_info']['4'])
            five_stars_number = int(data['stats_info']['star_info']['5'])

            star_flag = (
                            one_stars_number + two_stars_number + three_stars_number + four_stars_number + five_stars_number) > 0

            description = data['productInfo'][0]['productDescription']

            prices = ['"%s":%.2f' % (x, y) for x, y in datas.oneyear.prize(asin)]
            pricechart_data = '{' + ','.join(prices) + '}'


            #
            # pricechart_data = '[("2013-02-10","11"),'\
            #                    '("2013-02-11","6"),'\
            #                     '("2013-02-12","3"),'\
            #                     '("2013-02-13","2"),'\
            #                     '("2013-02-14","5"),'\
            #                     '("2013-02-15","3"),]'




            comments = ['"%s":%d' % (x, y) for x, y in datas.oneyear.comment(asin)]

            commentchart_data = '{' + ','.join(comments) + '}'

            # commentchart_data = '{"2013-02-10":11,' \
            #                     '"2013-02-11":6,' \
            #                     '"2013-02-12":3,' \
            #                     '"2013-02-13":2,' \
            #                     '"2013-02-14":5,' \
            #                     '"2013-02-15":3,' \
            #                     '"2013-02-16":8,' \
            #                     '"2013-02-17":6,' \
            #                     '"2013-02-18":6,}'

            mindata = ['"%s":%.2f' % (x, q) for x, y, z, q in datas.minmax.price_line_mm(asin)]
            maxdata = ['"%s":%.2f' % (x, y) for x, y, z, q in datas.minmax.price_line_mm(asin)]
            avgdata = ['"%s":%.2f' % (x, z) for x, y, z, q in datas.minmax.price_line_mm(asin)]



            minmaxaver_data = '[{"name":"Min","data":{' + ','.join(mindata) + '},' \
                              '{"name":"Max","data":{' + ','.join(maxdata) + '},' \
                              '{"name":"Average","data":{' + ','.join(avgdata) + '}]'

            # minmaxaver_data = '[{"name":"Min","data":' \
            #                   '{"2013-02-10":3,"2013-02-17":3,' \
            #                   '"2013-02-24":3,"2013-03-03":1,' \
            #                   '"2013-03-10":4}},' \
            #                   '{"name":"Max","data":' \
            #                   '{"2013-02-10":0,"2013-02-17":1,' \
            #                   '"2013-02-24":3,"2013-03-03":2,' \
            #                   '"2013-03-10":3,}},' \
            #                   '{"name":"Average","data":' \
            #                   '{"2013-02-10":0,"2013-02-17":1,' \
            #                   '"2013-02-24":2,"2013-03-03":2, ' \
            #                   '"2013-03-10":2}}]'

            kws = key_ana.asin_keywordAnalyse(asin)
            pos_list = ['["%s",%d]' % (k[0], k[1] * 100 / (k[1] + k[2])) for k in kws]
            negative_list = ['["%s",%d]' % (k[0], 100 - k[1] * 100 / (k[1] + k[2])) for k in kws]

            keyword_data = '[{name: "Positive",data: ' \
                           '[' + ','.join(pos_list) + ']},' \
                                                      '{	name: "Negative",data: ' \
                                                      '[' + ','.join(negative_list) + ']}]'

            return render_to_response("product.html", locals())
    return HttpResponse(jump_to_index_hmtl)


def product_d(request):
    if 'ASIN' in request.GET:
        asin = request.GET['ASIN']
        if asin != "":
            data = str(get_product_data(asin))
            return render_to_response("product_old.html", locals())
    return HttpResponse(jump_to_index_hmtl)


def source(request, type, path):
    # return HttpResponse('<html><script>location.assign("/static/' + type +'/'+path + '");</script></html>')
    return HttpResponseRedirect('/static/' + type + '/' + path)