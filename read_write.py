#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 23:43:56 2021

@author: jen
"""
import csv
with open('0717.csv') as f:
    mycsv=csv.reader(f)
    headers=next(mycsv)
    for row in mycsv:#row為list的資料型態
        print(row)
    
with open('0717.csv') as f:
    csvdic=csv.DictReader(f)
    for row in csvdic:
        print(row['Film'])
        
# In[1]:
#寫csv：
#先給所有欄位，內容用tuple，一筆資料一個tuple，所有資料用list格式儲存
headers = ['Film', 'Year', 'Actor', 'Director', 'Box Office', 'Budget', 'Bond Actor Salary']
rows = [('Dr. No','1962','Sean Connery', 'Terence Young','448.8', '7', '0.6'),
         ('From Russia with Love', '1963','Sean Connery','Terence Young','543.8','12.6','1.6')]
with open('0717-2.csv','w') as f:
    writecsv=csv.writer(f)
    writecsv.writerow(headers)
    writecsv.writerows(rows)
    
    
#用Dictionary方式寫入
rows = [{'Film':'Dr. No','Year': '1962', 'Actor': 'Sean Connery', 'Director': 'Terence Young', 'Box Office': '448.8', 'Budget':'7', 'Bond Actor Salary': '0.6'},
         {'Film': 'From Russia with Love', 'Year': '1963', 'Actor': 'Sean Connery', 'Director': 'Terence Young', 'Box Office': '543.8', 'Budget': '12.6', 'Bond Actor Salary': '1.6'},
         {'Film': 'Goldfinger', 'Year': '1964', 'Actor': 'Sean Connery', 'Director': 'Guy Hamilton', 'Box Office': '820.4', 'Budget': '18.6', 'Bond Actor Salary': '3.2'}]
with open('0717-3.csv','w') as f:
    writecsv=csv.DictWriter(f,headers)
    writecsv.writeheader()
    writecsv.writerows(rows)
    
    
# In[1]:
#json

import json

data={
      'name':'plusone',
      'height':155,
      'weight':40}

jsonstr=json.dumps(data,sort_keys=True,
           indent=5)#sort_key:字首排序
print(jsonstr)
#json.dumps : 用來將Python的資料類型編成JSON格式。
#dumps將這個dic轉成JSON的字串


data=json.loads(jsonstr)
print(data)
#json.loads : 將JSON物件轉為Python資料類型。


data={
      'one':True,
      'two':False,
      'three':None
      }

json_str=json.dumps(data,indent=3)
print(json_str)
# output
# {
#    "one": true,
#    "three": null,
#    "two": false
# }


from pprint import pprint
#pprint:讓loads後的資料排版比較好讀
data = {
    'one':True,
    'two':False,
    'three':
        {
        'text':[{'something': '2343488854324'},
            {'something': '2343453454354'}, 
            {'something': '1231242343545'},
            {'something': '3423423432113'}]
        }
}

pprint(data)

# In[1]:
import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.ptt.cc/bbs/NBA/index6500.html')
print(r.text)
soup=BeautifulSoup(r.text,'lxml')
#把回傳內容裡的文字也就是html內容傳入BeautifulSoup

a_tags=soup.select('div.r-list-container .title a')
for t in a_tags:
    print(t)

a_tags=soup.select_one('div.r-list-container .title a')
print(a_tags)
print(a_tags['href'])#取連結

with open('searchcontent.html','w+') as f:
    f.write(r.text)
    print('saved')
    
