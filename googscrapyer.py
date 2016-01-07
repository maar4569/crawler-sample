# -*- coding: utf-8 -*-

from __future__ import with_statement
import urllib2
import requests
from bs4 import BeautifulSoup

class Scrayper:

    def __init__(self):
        self.results = []

    def do(self,url):
        print url

   
if __name__ == "__main__":

    print u"main start!" 
     
    url = 'https://www.google.co.jp/search?q=ruby'
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    results_h = soup.findAll("h3", {'class':'r'})
    for link in results_h:
        related_url = link.a['href']
        print related_url
    print u"main finished"




