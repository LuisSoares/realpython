from flask import Flask,render_template,request,session,\
flash,redirect,url_for,g
from functools import wraps
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

#wrapper for making pages login required
def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if "logged_in" in session:
            return test(*args,**kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for("login"))
    return wrap
    
    
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
@login_required
def main():
    g.db=connect_db()
    cur=g.db.execute('select * from posts')
    posts=[dict(title=row[0],post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html',posts=posts)
    
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You are logged out')
    return redirect(url_for('login'))
    
#add posts
@app.route('/add',methods=['POST'])
@login_required
def add():
    title=request.form['title']
    post=request.form['post']
    if not title or not post:
        flash("All fields are required.Please try again.")
        return redirect(url_for("main"))
    else:
        g.db=connect_db()
        g.db.execute('INSERT INTO posts(title,post) VALUES (?,?)',
                     [request.form['title'],request.form['post']])
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted!')
        return redirect(url_for('main'))
        
    
    
    
if __name__=='__main__':
    app.run(debug=True)