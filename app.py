# -*- coding: utf-8 -*-
#---- Flask Hello World-----#
from flask import Flask
#create the application object
app=Flask(__name__)

#use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function which returns a string

def hello_world():
    return "Hello,World!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return "Hello {}".format(search_query)
    
@app.route("/integer/<int:value>")
def int_type(value):
    print value+1
    return "Correct"
    
@app.route("/float/<float:value>")
def float_type(value):
    print value+1
    return "Correct"
    
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"
    
    
if __name__=="__main__":
    app.run()
    