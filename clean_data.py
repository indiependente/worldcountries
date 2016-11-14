#!/usr/bin/python2

import os
import sys
import urllib2
import json
import unicodedata

filename = sys.argv[1]
regions = ['NA', 'APJ', 'EMEA', 'LATAM']
ws = 'http://restcountries.eu/rest/v1/name/'

if not os.path.isfile(filename):
	print 'File not found: ' + filename
	exit(1)

print 'Country, Region, Timezone'

with open(filename) as fp:
	for line in fp:
		splitted = line.split(',')
		name = splitted[0]
		if splitted[0][0] == '"':
			name += splitted[1]
			name = name.replace('"', '')
			region = splitted[6]
			subregion = splitted[7]
		else:
			region = splitted[5]
			subregion = splitted[6]
		
		country_info = json.loads(urllib2.urlopen(ws+name).read())[0]
		tz = []
		for t in country_info['timezones']:
			tz.append(unicodedata.normalize('NFKD', t).encode('ascii','ignore'))
		
		acronym = ''
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
				acronym = 'NA'
			else:
				acronym = 'LATAM'

		if acronym == '':
			continue

		print '%s, %s, %s' % (name, acronym, tz)