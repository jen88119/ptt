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

# sql = "INSERT INTO posts (post_id, url, title, time, body, author) VALUES (%s, %s, %s, %s, %s, %s)"
# val = ("1rgrgrgr", "rgrgrgrg", "vfvrgt", "gfgrgg", "wert", "grhyjy")
# mycursor.execute(sql, val)

# mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")
url="https://www.ptt.cc/bbs/Olympics_ISG/index.html"

def get_all_href(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    article_href = []
    results=soup.select("div.title a")
    for i in results:
        title=i.text
        if i:#可能會有文章刪除或不存在的可能，會得到None，所以需要先確認a_item是有值的，我們才取href
            print(title)
            article_href.append('https://www.ptt.cc'+i["href"])
            print('https://www.ptt.cc'+i["href"])
    print('----------next page-------------')
    return article_href

def get_article_content(article_url):#單篇文章頁面
    # over_date = 0
    r=requests.get(article_url)
    soup=BeautifulSoup(r.text,"lxml")
    results=soup.select('span.article-meta-value')
    if results:
        post_id = hashlib.md5(article_url.encode("utf-8")).hexdigest()
        author = results[0].text
        title = results[2].text
        time = results[3].text
        print('作者：',results[0].text)
        print('標題：',results[2].text)
        print('時間：',results[3].text)
        # Fri Jul 30 18:00:23 2021
        # if list[1] == 'Jul' and list[2] < 20 
        #    over_date = 1 
        comments = soup.select(".push")
        cmt_arr = []
        for cmt in comments:
            try:
                cmt_data = {}

                cmt_data['emotion'] = cmt.select('.push-tag')[0].text.strip()
                cmt_data['name'] = cmt.select('.push-userid')[0].text.strip()
                cmt_data['content'] = cmt.select('.push-content')[0].text[2:].strip()
                cmt_data['time'] = cmt.select('.push-ipdatetime')[0].text[-11:].strip()

                if cmt_data['emotion'] == '推' :
                    cmt_data['emotion'] = 1
                elif cmt_data['emotion'] == '→' :
                    cmt_data['emotion'] = 0
                else:
                    cmt_data['emotion'] = -1
                cmt_arr.append(cmt_data)
                      
                sql = "INSERT IGNORE INTO comments (emotion, name, content, time, post_id ) VALUES (%s, %s, %s, %s, %s)"
                val = (cmt_data['emotion'], cmt_data['name'], cmt_data['content'], cmt_data['time'], post_id)
                mycursor.execute(sql, val)
                mydb.commit()

            except:
                pass
        # print(cmt_arr)
        body = soup.find('div',{'id':'main-content'})
        for child in body.select("*"):
            child.decompose()#刪掉被標籤包住的
        sql = "INSERT IGNORE INTO posts (post_id, url, title, time, body, author) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (post_id, article_url, title, time, body.get_text().strip(), author)
        mycursor.execute(sql, val)
        mydb.commit()
    # return over_date


       
# while True:
for page in range(1,10):
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    btn=soup.select('div.btn-group > a')#取出緊連 div.btn-group 下面的a
    
    up_page_url=btn[3]['href']
    next_page_url='https://www.ptt.cc'+up_page_url
    url=next_page_url
    urls=get_all_href(url=url)
    # is_over = 0
    for item in urls:
        get_article_content(article_url=item)
        # a = get_article_content(article_url=item)
        # if a == 1:
        #   is_over = 1
        #   break
    # if is_over == 1:
    #    break
# print("finish!!")
           
       
        
        
        
        