#!/usr/bin/python2

import urllib2
import json
import unicodedata


regions = ['AMS', 'APJ', 'EMEA', 'LATAM']
api = 'http://restcountries.eu/rest/v1/all'


print 'Country, Region, Currencies'

def u2a(ustr):
	return unicodedata.normalize('NFKD', ustr).encode('ascii','ignore')

countries = json.loads(urllib2.urlopen(api).read())

for c in countries:

	currs = ''
	for cu in c['currencies']:
		if currs != '':
			currs += '_'
		currs += u2a(cu)
	

	acronym = ''
	region = c['region']
	subregion = c['subregion']
	
	if region == 'Europe' or region == 'Africa':
		acronym = 'EMEA'
	elif region == 'Asia':
		if 'Western' in subregion:
			acronym = 'EMEA'
		else:
			acronym = 'APJ'
	elif region == 'Oceania':
		acronym = 'APJ'
	elif region == 'Americas':
		if 'Northern' in subregion:
			acronym = 'AMS'
		else:
			acronym = 'LATAM'

	if acronym == '':
		continue

	print '%s, %s, %s' % (u2a(c['name']), acronym, currs)