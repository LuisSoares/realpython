from flask import Flask,render_template,request,session,\
flash,redirect,url_for,g

import sqlite3

#Configuration
DATABASE='blog.db'
USERNAME='admin'
PASSWORD='admin'
SECRET_KEY='iJs\xb2\xae~\xd91\r\xc2\xff;\xe2\xd5\xb5\xcc\x0f\xef[\x0bTYD\x04'


app=Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
#app.config is an object like a dictionary but with other methods

app.config.from_object(__name__)

#connection to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
test='test of error'
@app.route('/',methods=['GET','POST'])
def login():
    error=None
    test='Test of error'
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME'] or \
        request.form['password']!=app.config['PASSWORD']:
            error='Invalid Credentials. Please try again.'
        else:
            session['logged_in']=True
            return redirect(url_for('main'))
     #you have to pass the variables that are used in the template
    return render_template('login.html',error=error)
    
@app.route('/main')
def main():
    return render_template('main.html')
    
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You are logged out')
    return redirect(url_for('login'))
    
if __name__=='__main__':
    app.run(debug=True)