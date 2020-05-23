"""
数据库写操作
"""
import pymysql
# 连接数据库
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
# 生成游标
cur =db.cursor()
# 写数据库操作
# name = input("请输入姓名：")
# sex = input("请输入性别(w/m)：")
# age = input("请输入年龄：")
# score = input("请输入成绩：")
# try:
#     # sql='insert into cls (name,sex,age,score)
#     # values ("%s","%s",%s,%s);'%(name,sex,age,score)
#     # 方法2
#     sql = 'insert into cls (name,sex,age,score) values (%s,%s,%s,%s);'
#     cur.execute(sql,[name,sex,age,score]) # 执行sql语句  (不能给sql语句传递关键字，表名，字段名，符号)
#     db.commit()  # 将写操作结果提交到数据库
# except Exception as e:
#     print(e)
#     db.rollback() # 一旦出错则回滚 到 语句执行之前的状态
student = [
    ("sfr","w",16,81),
    ("sfj","w",17,80),
    ("sfl","m",18,79)
]
try:
    # for i in student:
    #     sql = 'insert into cls (name,sex,age,score) values (%s,%s,%s,%s);'
    #     cur.execute(sql,i)
    sql = 'insert into cls (name,sex,age,score) values (%s,%s,%s,%s);'
    cur.executemany(sql,student) # 执行sql语句  (不能给sql语句传递关键字，表名，字段名，符号)
    db.commit()  # 将写操作结果提交到数据库
except Exception as e:
    print(e)
    db.rollback()


# 使用完毕
cur.close()
db.close()