# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 05:33:59 2018

@author: kdabhadk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import urllib
from bs4 import BeautifulSoup


def get_data():
    source=urllib.request.urlopen('https://www.exchangerates.org.uk/USD-INR-exchange-rate-history.html')
    html=source.read()
    
    soup = BeautifulSoup(html,"lxml")
    #(soup.prettify())
    soup.a
    
    data_table=soup.find('table',{"id":'hist'})
    #print (data_table)
    
    day=[]
    rate=[]
    
    for counter,row in enumerate(data_table.findAll('tr')):
        cells=row.findAll('td')
        if len(cells)==3:
            day.append(((cells[0].find(text=True)).split(None,1))[1])
            rate.append(float(((cells[1].find(text=True)).split(' '))[3]))
            
    date=[]
    for counter,object_ in enumerate(day):
        date.append(pd.datetime.strptime(object_, "%d %B %Y"))
        
    rate_data=pd.DataFrame({'Day':date,'Rate':rate})
    rate_data=rate_data.set_index('Day')
    rate_data_full=rate_data.reindex(index=rate_data.index[::-1])
    
    return rate_data_full


