import mysql.connector        
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database='olmpic',
)
 
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
    print(x)

sql = "INSERT INTO posts (post_id, url, title, time, body, author) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("1rgrgrgr", "rgrgrgrg", "vfvrgt", "gfgrgg", "wert", "grhyjy")
mycursor.execute(sql, val)

mydb.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")