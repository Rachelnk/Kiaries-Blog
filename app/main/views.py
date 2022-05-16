from flask import render_template, request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PostForm,CommentsForm, UpdateProfile
from ..models import User, Comment, Blog_Post
from .. import db, photos