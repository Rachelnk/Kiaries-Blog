from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import InputRequired,Email,EqualTo, ValidationError
from ..models import Blog_Post, Comment

class PostForm(FlaskForm):
  title = StringField ('Title', validators= [InputRequired()])
  content = TextAreaField('Content',validators=[InputRequired()])
  submit = SubmitField('Add Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on the post',validators=[InputRequired()])
    submit = SubmitField('Add Comment')
class SubscriberForm(FlaskForm):
    email = StringField('Enter Your Email Address', validators=[InputRequired(),Email()])
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a bit about yourself',validators=[InputRequired()])
    submit = SubmitField('Add Bio')
class EditPostForm(FlaskForm):
    update_title = StringField ('Title', validators= [InputRequired()])
    update_content = TextAreaField('Content',validators=[InputRequired()])
    submit = SubmitField('Edit Post')

