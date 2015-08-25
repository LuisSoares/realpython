# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:08:09 2015

@author: luis
"""

import sqlite3

with sqlite3.connect("newnum.db") as connection:
    cursor=connection.cursor()
    while True:
        a=int(raw_input("1-Average\n2-Maximum\n3-Minimum\n4-Sum\n5-exit\n"))
        if a==5:break
        elif a in [1,2,3,4]:
            operations={1:'avg',2:'max',3:'min',4:'sum'}
            cursor.execute("SELECT {}(num) from numbers".format(operations[a]))
            get=cursor.fetchall()
            print("{}->{}\n".format(operations[a],get[0][0]))
        else:continue