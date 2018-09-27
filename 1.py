# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 09:12
# @Author  : zqj
# @FileName: 1.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com


import pymysql

config = {
    'host' : 'localhost',
    'user' : 'root',
    'passwd' : 'zqjstc0504',
    'port' : 3306,
    'db' : 'zqjstudy'
}
conn = pymysql.connect(**config)
cursor = conn.cursor()
#查询"01"课程比"02"课程成绩高的学生的信息及课程分数
sql = '''
select a.* , c.*
from
(select a.* from
	(select * from sc where sc.c = '01')a
	left join
	(select * from sc where sc.c = '02')b
	on a.s = b.s
	where a.score > b.score)a, student c
where a.s = c.s
'''
cursor.execute(sql)
print(cursor.fetchall())
