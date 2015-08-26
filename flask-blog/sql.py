# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:09:26 2015

@author: luis
"""

import sqlite3

with sqlite3.connect("blog.db") as connection:
    c=connection.cursor()
    c.execute("CREATE TABLE posts (title TEXT,post TEXT)")
    c.execute('INSERT into posts VALUES("GOOD","I\'m good")')
    c.execute('INSERT into posts VALUES("WELL","I\'m well")')
    c.execute('INSERT into posts VALUES("EXCELLENT","I\'m excellent")')
    c.execute('INSERT into posts VALUES("OKAY","I\'m okay")')
    
    
    