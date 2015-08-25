# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:54:10 2015

@author: luis
"""

import sqlite3

#create a new database if the database doesn't already exist
conn=sqlite3.connect('new.db')
#conn=sqlite3.connect(":memory:")

#get a cursor object
cursor=conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City',\
'NY',8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco',\
'CA',80000)")

conn.commit()
conn.close()
