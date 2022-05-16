from flask import render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PostForm,CommentsForm, UpdateProfile, EditPostForm
from ..models import User, Comment, Blog_Post
from .. import db, photos

@main.route('/')
def index():
    all_posts = Blog_Post.query.all()
    title = 'Home -  Welcome to Kiarie\'s Blog'
    return render_template('index.html')

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_post():
    form = PostForm
    if form.validate_on_submit():
        title = form.title.data
        content = form.post.data
        user_id = current_user
        new_post_object = Blog_Post(content = content ,user_id=current_user._get_current_object().id,title=title)
        new_post_object.save_post()
        return redirect(url_for('main.index'))
    return render_template('add_post.html', form = form)


@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    form = CommentsForm()
    post = Blog_Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,post_id = post_id)
        new_comment.save_comments()
        return redirect(url_for('.comment', post_id = post_id))
    return render_template('comment.html', form =form, post = post,all_comments=all_comments)

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog_Post.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)

@main.route('/user/<name>/editpostform', methods = ['POST','GET'])
@login_required
def editpostform(name):
    form = EditPostForm()
    blogpost = Blog_Post.query.filter_by(username = name).first()
    if blogpost == None:
        abort(404)
    if form.validate_on_submit():
        blogpost.update_title = form.update_title.data
        blogpost.update_content = form.update_content.data
        blogpost.save_user()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/post.html',form =form)