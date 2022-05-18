from email.policy import default
from . import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
class User (db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key =True)
  username = db.Column (db.String(255), unique = True, nullable = True)
  email = db.Column (db.String(255), unique = True, nullable = True)
  bio = db.Column (db.String(255),nullable = True)  
  profile_pic = db.Column (db.String(255),nullable = True)
  password_secure = db.Column(db.String(255))
  blog_post = db.relationship('Blog_Post', backref='user', lazy='dynamic')
  comment = db.relationship('Comment' , backref = 'user', lazy = 'dynamic')
  


  @property
  def set_password(self):
    raise AttributeError('You cannot read the password attribute')
  @set_password.setter
  def password(self, password):
    self.password_secure = generate_password_hash(password)
  
  def verify_password(self, password):
    return check_password_hash(self.password_secure, password)
  def save_user(self):
      db.session.add(self)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
  
  def __repr__(self):
      return f'User{self.username}'

class Blog_Post(db.Model):
      '''
      model that contains database schema for blog post table
      '''
      __tablename__ = 'posts'
      id = db.Column(db.Integer, primary_key = True)
      title = db.Column(db.String(255), nullable = False)
      content = db.Column(db.Text(), nullable = False)
      time_posted = db.Column (db.DateTime, default=datetime.utcnow)
      user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
      comment = db.relationship('Comment' , backref = 'blog_post', lazy = 'dynamic')

      def save_post(self):
      
          db.session.add(self)
          db.session.commit()

      def delete(self):
        db.session.delete(self)
        db.session.commit()

      
      def get_blog(id):
        blog = Blog_Post.query.filter_by(id=id).first()

        return blog

      def __repr__(self):
        return f'Blog_Post {self.title}'


class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer(), primary_key =  True)
  comment = db.Column(db.String)
  time_posted = db.Column(db.DateTime, default=datetime.utcnow)
  blog_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save(self):
        db.session.add(self)
        db.session.commit()

  def delete(self):
       db.session.remove(self)
       db.session.commit()

  def get_comment(id):
      comment = Comment.query.all(id=id)
      return comment


  def __repr__(self):
      return f'Comment {self.comment}'

class Subscriber(db.Model):
    __tablename__='subs'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




