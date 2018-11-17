# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 23:09
# @Author  : zhushaoxin
# @Email   : 185250613@qq.com
# @File    : sqlite.py

import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()
