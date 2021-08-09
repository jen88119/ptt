# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import mysql.connector
import hashlib        
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database='olmpic',
)
 
mycursor = mydb.cursor()

sql="SELECT post_id,title,body FROM posts"

mycursor.execute(sql)

all_posts = mycursor.fetchall()
all_records = []

for x in all_posts:
    print(x)
    # post = {}
    # post['title'] = x[1]
    # post['body'] = x[2]
    # post['comments'] = []
    # pid = x[0]
    # sql="SELECT content FROM comments WHERE post_id='"+pid+"'"
    # mycursor.execute(sql)
    # all_comments = mycursor.fetchall()
    # for cmt in all_comments:
    #     post['comments'].append(cmt[0])
    # all_records.append(post)
# print(all_records)