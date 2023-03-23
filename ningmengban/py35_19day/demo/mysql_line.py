import pymysql

con = pymysql.connect(
    host='api.lemonban.com',
    port=3306,
    user='future',
    password='123456',
    charset='utf8'
)
# cur = conect.cursor()
# sql = 'use future;'
# res = cur.execute(sql)
# conect.commit()
with con as cur:
    sql = "select * from future.member limit 5;"
    res = cur.execute(sql)
    #获取查寻集中的所有内容
    res = cur.fetchall()
    #获取查询集中的第一条数据
    # result = cur.fetchone()

# cur.close()
# con.close()
# print(result)
print(res)

