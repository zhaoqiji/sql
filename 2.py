# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 21:59
# @Author  : zqj
# @FileName: 2.py.py
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
#查询"01"课程比"02"课程成绩低的学生的信息及课程分数
# in 和=的主要区别在于in可以加多个，=较快
sql = '''
select a.* , c.*
from
(select a.* from
	(select * from sc where sc.c in ('01'))a
	left join
	(select * from sc where sc.c in ('02'))b
	on a.s = b.s
	where a.score < b.score)a, student c
where a.s = c.s
'''
cursor.execute(sql)
print(cursor.fetchall())
