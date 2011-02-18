#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, urllib2
socket.setdefaulttimeout(35)
http_headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.12) Gecko/20101027 Ubuntu/10.04 (lucid) Firefox/3.6.12",\
                "Accept":"text/html"}

import re
RE_elenco_compositori = re.compile('^href="/cidim/content/.*db=bdci&id=.*">$')
RE_info_compositore = re.compile('.*<div style="background:.*;padding:2px 5px 2px 5px;" class="size_12"> <span style="color:.*;font-weight:bold">.*: </span>(.*) </div>')
RE_nome_compositore = re.compile('<h1 class="title" style="color:#ff9900;border-bottom:2px solid #ff9900;margin:0" align="center">(.*)</h1>')
RE_email_compositore = re.compile('.*<a href="mailto:.*">(.*)</a>.*')

def estrapola_pagina(lettera, numero_pagina):
    URL = 'http://www.cidim.it/cidim/content/314618?db=bdci&p=%s&dest=C&tp=N&lett=%s' % (numero_pagina, lettera)
    try:
        pagina_html = urllib2.urlopen( urllib2.Request(URL, None, http_headers) ).read()
    except:
        print 'Impossibile leggere la pagina', URL
        return False

    url_artisti = set()

    for parola in pagina_html.split():
        if RE_elenco_compositori.match(parola):
            url_artisti.add(parola)

    for compositore in url_artisti:
        estrai_dati_compositore('http://www.cidim.it'+compositore[6:-2])

def estrai_dati_compositore(URL):
    try:
        pagina_html = urllib2.urlopen( urllib2.Request(URL, None, http_headers) ).read()
    except:
        print 'Impossibile leggere compositore', URL
        return False

    for riga in pagina_html.split('\n'):
        m = RE_info_compositore.match(riga)
        if m:
            print '"'+m.group(1)+'",',
            continue

        m = RE_nome_compositore.match(riga)
        if m:
            print '"'+m.group(1)+'",',
            continue

        m = RE_email_compositore.match(riga)
        if m:
            print '"'+m.group(1)+'"',
            continue

    print

if __name__ == "__main__":
    import string

    for lettera in string.letters[26:]: #genero tutte le combinazioni iniziali/pagine
        for numero_pagina in range(9):
            estrapola_pagina(lettera, numero_pagina)
