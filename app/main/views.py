from flask import Flask
from flask import render_template,redirect,request
from flask.helpers import url_for
from .forms import PostForm
from ..models import Post
from . import main
from flask import app
from .. import db

post = Post
form = PostForm

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('index.html', title = title)

@main.route('/login', methods = ['GET','POST'])
def login():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    title = "One min pitch"
    return render_template('login.html', title = title)

@main.route('/post', methods = ['GET','POST'])
def addpost():
    '''
    View post page
    '''

    if request.method == 'POST':
        title = request.form["title"]
        content = request.form["content"]

        new_post = Post(title,content)
        new_post.save_post()
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))

    results = Post.query.all()

    title = "One min pitch"
    return render_template('post.html', title = title, results=results, form = form)

