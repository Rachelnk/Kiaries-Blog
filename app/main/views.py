from flask import render_template, request,redirect,url_for, abort, flash
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PostForm,CommentsForm, UpdateProfile, EditPostForm
from ..models import User, Comment, Blog_Post, Subscriber
from .. import db
from ..requests import get_random_quote
from datetime import datetime
#  photos
@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog_Post.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))

@main.route('/')
def index():
    page = request.args.get('page', 1, int)
    posts = Blog_Post.query.order_by(Blog_Post.time_posted.desc()).paginate(page = page, per_page = 3)
    quote = get_random_quote()
    
    title = 'Home -  Welcome to Kiarie\'s Blog'
    # if request.method == "POST":
    #     new_sub = Subscriber(email = request.form.get("subscriber"))
    #     db.session.add(new_sub)
    #     db.session.commit()
    #     welcome_message("Thank you for subscribing to Kiaries blog", 
    #                     "email/welcome", new_sub.email)
    return render_template('index.html' , posts = posts, quote = quote)

@main.route('/new_post', methods = ['POST','GET'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user
        post_by = current_user.username
        new_post_object = Blog_Post(content = content ,user_id=current_user._get_current_object().id,title=title,
        time_posted = datetime.now())
        new_post_object.save_post()
        # subs = Subscriber.query.all()
        # for subs in subs:

        return redirect(url_for('main.index'))
    return render_template('add_post.html', form = form)

@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog_Post.query.get(id)
    return render_template('blog.html',blog=blog,comments=comments)


@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    blog = Blog_Post.query.get(blog_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog',id = blog.id))

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
    return render_template('profile/edit_blogpost.html',form =form)

# @main.route('/user/<name>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(name):
#     user = User.query.filter_by(username = name).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',name=name))
@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page',1, type = int )
    blogs = Blog_Post.query.filter_by(user=user).order_by(Blog_Post.posted.desc()).paginate(page = page, per_page = 4)
    return render_template('userposts.html',blogs=blogs,user = user)