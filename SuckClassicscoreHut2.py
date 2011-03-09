#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, urllib2, os, urllib
try:
	from BeautifulSoup import BeautifulSoup
except:
	print "Installa il package BeautifulSoup"
	import sys
	sys.exit()

for lettera in string.letters[26:]:
	print 'Elaboro lettera',lettera
	url_base='http://www.classicscore.hut2.ru/%s.html' % (lettera,)

	html = urllib2.urlopen(url_base).read()

	s=BeautifulSoup(html)

for tag in s.findAll('a'):
	url = tag.attrs[0][1]
	nome = tag.text+'.pdf'
	if 'scorage' in url:
		print 'Scarico',url
		try:
			urllib.urlretrieve(url,'/tmp/'+nome)
		except:
			print 'Sbajato',url
