#-*- coding:utf-8 -*-

import urllib
import simplejson as json

REQUEST_URL = 'http://112.124.1.3:8004'

def get_all_category():
	'''
	get all categories
	'''
	all_category_url = 'api/commodity'
	
	#use json.loads to convert str to json obj
	#also can use eval() or other funcs
	data = json.loads(urllib.urlopen('/'.join([REQUEST_URL,
		all_category_url])).read())
	for single_cate in data:
		print single_cate['name']

def get_avaliable_fields():
	'''
	view all get avaliable fields
	'''
	fileds_url = 'api/commodity/field'
	data = json.loads(urllib.urlopen('/'.join([REQUEST_URL,
		fileds_url])).read())
	print [field for field in data]



def get_specified_commodity():
	'''
	get specified commodity given 
	category or asin
	'''
	all_category_url = 'api/commodity'

	all_category_data = json.loads(urllib.urlopen('/'.join([
		REQUEST_URL, all_category_url])).read())

	#take first category
	specified_cate_data = json.loads(urllib.urlopen('?'.join([
		'/'.join([REQUEST_URL, all_category_url]),
		urllib.urlencode({
			'category_name': all_category_data[0]['name'],
			'field': ['ASIN'],
			})])).read())
	#take specified asin to get detail data
	#get all field also can get specify-field data
	single_commodity_review = []
	for i in xrange(3):
		single_commodity_review += json.loads(urllib.urlopen('?'.join(
		    ['/'.join([REQUEST_URL, 'api/commodity', specified_cate_data[0]['ASIN']]),
		    urllib.urlencode({'field': ['ASIN', 'review']}) ])).read())['review']
	#print single_commodity
	#print length of review
	print len(single_commodity_review)
	
	for review in single_commodity_review:
		pass
	
def review_info():
	all_category = 'api/commodity'
	

if __name__ == '__main__':
	#get_all_category()
	get_specified_commodity()