from flask import render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PostForm,CommentsForm, UpdateProfile
from ..models import User, Comment, Blog_Post
from .. import db, photos

@main.route('/')
def index():
    all_posts = Blog_Post.query.all()
    title = 'Home -  Welcome to Kiarie\'s Blog'
    return render_template('index.html')

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PostForm
    if form.validate_on_submit():
        title = form.title.data
        content = form.post.data
        user_id = current_user
        new_post_object = Blog_Post(content = content ,user_id=current_user._get_current_object().id,title=title)
        new_post_object.save_post()
        return redirect(url_for('main.index'))
    return render_template('add_post.html', form = form)