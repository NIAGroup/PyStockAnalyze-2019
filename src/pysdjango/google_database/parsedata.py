import pprint as pp
import requests
import xmltodict
import json
from bs4 import BeautifulSoup
from .models import Articles
from .googleapi import *
from .summary import *

class Parse:
    summ = Summary()
    
    
    def run(self, inputText):
        rss = CSEQuery.cse_news_search(inputText)
        test = xmltodict.parse(rss)

        #print(test['rss']['channel']['item'][0])

        for i in range(0,10): #Grav first 10 documents from RSS feed
            art = Articles()
            for key,value in test['rss']['channel']['item'][i].items():
                if(key == 'title'):
                    art.title = value
                elif(key == 'link'):
                    art.urlSrc = value
                elif(key == 'description'):
                    art.description = BeautifulSoup(value,features="html.parser").text
            try:    
                art.summary = self.summ.sumText(art.urlSrc)
            except:
                art.summary = "No description."
            art.save()

