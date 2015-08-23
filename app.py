# -*- coding: utf-8 -*-
#---- Flask Hello World-----#
from flask import Flask
#create the application object
application=Flask(__name__)

#use decorators to link the function to a url
@application.route("/")
@application.route("/hello")

#define the view using a function which returns a string

def hello_world():
    return "Hello,World!"
    
if __name__=="__main__":
    application.run()
    