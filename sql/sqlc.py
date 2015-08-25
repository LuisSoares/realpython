# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:45:46 2015

@author: luis
"""

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor=connection.cursor()
    cities=[("Boston","MA",600000),
            ("Chicago",'IL',2700000),
            ("Houston",'TX',2100000),
            ('Phoenix','AZ',1500000)]
            
    cursor.executemany('INSERT INTO population VALUES(?,?,?)',cities)
    