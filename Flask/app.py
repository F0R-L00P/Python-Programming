import os
os.chdir(r'C:\Users\Flask')

import sqlite3
from datetime import datetime

# import flask library
from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

# build flask constructor
# using name to reference file
app = Flask(__name__)

# tell flask where the database is going to be stored.
# this can be done via configuration
    #this is the path where the database is stored
    #sqlalchemy allows us to use any database we want - here we are using sqlite
    #once db is chosen define path where you want it stored
        #/// is relative path
        #//// is absolute path
        #lets create database file named posts
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #can swap mysql, or postsql
db = SQLAlchemy(app) #sqlalchemy took the app and linked it to the database sqlite 

# lets design the database
# each class variable is considered a piece of data in our database
class BlogPost(db.Model):
    # define all things a post might have
    
    #primary key means id is the main distinguisher between blog posts
    id = db.Column(db.Integer, primary_key=True) #define column and provide datatype
    
    #use title of string upto 100 characters
    #the field is REQUIRED and cannot be null
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default='N/A') #author is required, and can't be null, if non provided default to N/A
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)#default date is "now"

    def __repr__(self): #print-out whenever we print a new blogpost
        return 'Blog post ' + str(self.id)


#####Create db#####
# to create the db, go to python environment
    # from app import db
    # db.create_all() --> this will create database with model in mind, db is now in directory
    #can use model that needs to be imported....
        # from app import BlogPost
        # view using BlogPost.query.all() --> at first this should be a empty list
    #lets add data to the databade
        #db.session.add(BlogPost(title = 'Blog Pos 1', content = 'Content of BP 1', author = 'BEN'))
        #BlogPost.query.all()
    #add another entry
        #db.session.add(BlogPost(title = 'Blog Pos 2', content = 'Content of BP 2', author = 'JACK'))
        #BlogPost.query.all()
    #can access values with list indexing
        #BlogPost.query.all()[0].author
        ##BlogPost.query.all()[0].date_posted   
####



# use html template in code by rendering it
# file MUST be in directory named "templates" inorder to be found
# browser can also return raw html, but better to render it
@app.route('/')
def index():
    return  render_template('index.html')

# allow both get and post from the page
# posting will allow database capture of information 
@app.route('/posts', methods=['GET','POST'])
def posts():
    # if method is post, read all data from the post and send it to the database
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        #create blogpost object
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)
        # add post to DB
        #connection = sqlite.connect('posts.db', timeout=1)
        db.session.add(new_post)
        db.session.commit() #commit input to DB
        return redirect('/posts') #redirect to page and display
    else: #display blogposts as normal without adding anything 
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all() #get all posts from the DB
        return render_template('posts.html', posts=all_posts)

##Can Delete posts or make changes
# get the query you want to delete and pass the session and delete it
# the deletion will only take plac if the session is commited
# db.session.delete(BlogPost.query.get(2)) --> this gives you blogpost #2
# db.session.delete(BlogPost.query.get(2)) --> delete via the object
# db.session.commit()

# can use the same method to make direct changes to the query
# db.session.get(2).author = 'JACK'
# db.session.commit()

# can filter using 
# BlogPost.query.filter_by(author = 'BEN').all()
###################

# lets define a new route for deleting posts
# define which url to delete via the id
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id) #if the id doesnt exit, it wont break
    db.session.delete(post) # delete post
    db.session.commit() # commit session for post to delete
    return redirect('/posts') # after delete redirect back to post page

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST']) #when editing, your getting-revising-and posting after
def edit(id):

    post = BlogPost.query.get_or_404(id) #if the id doesnt exit, it wont break
    
    if request.method == 'POST':
        
        post.title = request.form['title'] # get data on title field and save it to post.title
        post.content = request.form['content'] 
        post.author = request.form['author']
        db.session.commit() # commit changes
        return redirect('/posts') #after edit redirect to post page
    else:
        return render_template('edit.html', post=post)


# define urls by routing
# whatever in the url will display in the page - i.e. writing name BEN 
# dynamic url int, string etc.
    # /home/user/<string:name>/posts/<int:id>
    # url would be http://localhost:5000/home/users/BEN/posts/77 -> id number
@app.route('/home/<string:name>') # base index
# code will be run when getting the url
def hello(name):
    # return 'Hello, " + name + ", your id is: " + str(id)
    return "HELLO " + name + "!!!" # whenever url is run, text will be displayed in webpage

@app.route('/onlyget', methods=['GET']) # only allow get, if method is post can't change value
def get_only():
    return 'You can only get this webpage. 3'


if __name__ == "__main__":
    # turn on debug mode to find errors
    app.run(debug=True)

# can run - python app.py from cmd on the directory
# can run directly from IED, since debug mode is on, you can just refresh server
# without running the code again, make changes and save code -- refresh page to see changes


# templets are the front end of flask
