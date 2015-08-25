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
@app.route("/test")
def search():
    return "Hello"
    
if __name__=="__main__":
    app.run()
    