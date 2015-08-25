# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:04:10 2015

@author: luis
"""

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c=connection.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
        