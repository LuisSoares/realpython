# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:54:10 2015

@author: luis
"""

import sqlite3

#create a new database if the database doesn't already exist
conn=sqlite3.connect('new.db')

#get a cursor object
cursor=conn.cursor()

cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)""")

conn.close()
