#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, urllib2, os, urllib, socket, time, shutil
try:
	from BeautifulSoup import BeautifulSoup
except:
	print "Installa il package BeautifulSoup"
	import sys
	sys.exit()

socket.setdefaulttimeout(35)
tank='/home/mic/'

for lettera in string.letters[26:]:
	print 'Elaboro lettera',lettera
	url_base='http://www.classicscore.hut2.ru/%s.html' % (lettera,)

	print 'fetch'
	html = urllib2.urlopen(url_base).read()

	s=BeautifulSoup(html)

	print 'tag'
	for tag in s.findAll('a'):
	url = tag.attrs[0][1]
	nome = tag.text+'.pdf'
	if 'scorage' in url:
		#print 'Scarico',url
		if not os.path.isfile(tank+nome):
			try:
			urllib.urlretrieve(url,'/tmp/.temporaneo_score.pdf')
			shutil.move('/tmp/.temporaneo_score.pdf',tank+nome)
			print 'scaricato',nome
			except:
			print '                 Sbajato',url,nome
			open('riscarica.txt','a').write(url+' '+nome+' \n')
			time.sleep(30)
		else:
			print 'Salto',nome
