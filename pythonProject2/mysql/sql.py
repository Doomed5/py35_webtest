import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='0305',
                       database='python',
                       charset='utf8')
cursor = conn.cursor()
sql = 'select * from students where id=1;'
cursor.execute(sql)
result = cursor.fetchall()
print(result)

