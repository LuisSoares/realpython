# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:53:09 2015

@author: luis
"""

import sqlite3

"""with sqlite3.connect("new.db") as connection:
    cursor=connection.cursor()
    for row in cursor.execute("SELECT city,state FROM population"):
        print row"""
        
"""with sqlite3.connect("new.db") as connection:
    cursor=connection.cursor()
    cursor.execute("SELECT city,state FROM population")
    rows=cursor.fetchall()
    for r in rows:
        print r[0],r[1]"""
    
        
with sqlite3.connect("new.db") as connection:
    cursor=connection.cursor()
    cursor.execute("UPDATE population SET population=9000000 WHERE city='New York City'")
    cursor.execute("DELETE FROM population WHERE city='Boston'")
    print('\nNEW DATA\n')
    cursor.execute("SELECT * FROM population")
    rows=cursor.fetchall()
    for r in rows:
        print r[0],r[1],r[2]
        
        