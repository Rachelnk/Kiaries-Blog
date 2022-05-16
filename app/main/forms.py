from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import InputRequired
from ..models import Blog_Post, Comment

class PostForm(FlaskForm):
  title = StringField ('Title', validators= [InputRequired()])
  content = TextAreaField('Content',validators=[InputRequired()])
  submit = SubmitField('Add Pitch')