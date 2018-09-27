# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 21:39
# @Author  : zqj
# @FileName: mysql50.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

import pymysql

#conn = pymysql.connect(config)
try:
    conn = pymysql.connect(host = 'localhost',user = 'root',passwd = 'zqjstc0504',db = 'zqjstudy')
    cursor = conn.cursor()
except Exception as e:
    print(e)


#创建测试数据
sql = 'create table Student(S varchar(10), Sname varchar(10),Sage datetime, Ssex nvarchar(10))'
try:
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
# sql = 'select * from student'
# try:
#     cursor.execute(sql)
#     a = cursor.fetchall()
# except Exception as e:
#     print(e)
# print(a)

sql0 = "insert into Student values('01' , '赵雷' , '1990-01-01' , '男')"
sql1 = "insert into Student values('02' , '钱电' , '1990-12-21' , '男')"
sql2 = "insert into Student values('03' , '孙风' , '1990-05-20' , '男')"
sql3 = "insert into Student values('04' , '李云' , '1990-08-06' , '男')"
sql4 = "insert into Student values('05' , '周梅' , '1991-12-01' , '女')"
sql5 = "insert into Student values('06' , '吴兰' , '1992-03-01' , '女')"
sql6 = "insert into Student values('07' , '郑竹' , '1989-07-01' , '女')"
sql7 = "insert into Student values('08' , '王菊' , '1990-01-20' , '女')"
sql8 = "create table Course(C varchar(10), Cname varchar(10),T varchar(10))"
sql9 = "insert into Course values('01' , '语文' , '02')"
sql10 = "insert into Course values('02' , '数学' , '01')"
sql11 = "insert into Course values('03' , '英语' , '03')"
sql12 = "create table Teacher(T varchar(10),Tname varchar(10))"
sql13 = "insert into Teacher values('01' , '张三')"
sql14 = "insert into Teacher values('02' , '李四')"
sql15 = "insert into Teacher values('03' , '王五')"
sql16 = "create table SC(S varchar(10),C varchar(10),score decimal(18,1))"
sql17 = "insert into SC values('01' , '01' , 80)"
sql18 = "insert into SC values('01' , '02' , 90)"
sql19 = "insert into SC values('01' , '03' , 99)"
sql20 = "insert into SC values('02' , '01' , 70)"
sql21 = "insert into SC values('02' , '02' , 60)"
sql22 = "insert into SC values('02' , '03' , 80)"
sql23 = "insert into SC values('03' , '01' , 80)"
sql24 = "insert into SC values('03' , '02' , 80)"
sql25 = "insert into SC values('03' , '03' , 80)"
sql26 = "insert into SC values('04' , '01' , 50)"
sql27 = "insert into SC values('04' , '02' , 30)"
sql28 = "insert into SC values('04' , '03' , 20)"
sql29 = "insert into SC values('05' , '01' , 76)"
sql30 = "insert into SC values('05' , '02' , 87)"
sql31 = "insert into SC values('06' , '01' , 31)"
sql32 = "insert into SC values('06' , '03' , 34)"
sql33 = "insert into SC values('07' , '02' , 89)"
sql34 = "insert into SC values('07' , '03' , 98)"
for i in range(35):
    try:
        eval('cursor.execute(sql{})'.format(i))
    except Exception as e:
        print(e)
conn.commit()