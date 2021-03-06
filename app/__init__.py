from ensurepip import bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from config import config_options
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail ()
# photos = UploadSet('photos', IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
  app = Flask(__name__)
  
  # initializing flask extensions
  db.init_app(app)
  bootstrap.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)
  # configure UploadSet
  # configure_uploads(app,photos)

  # Creating the app configurations
  app.config.from_object(config_options[config_name])
  # Registering the blueprint
  from .main import main as main_blueprint
  from .auth import auth as authentication_blueprint
  app.register_blueprint(main_blueprint)
  app.register_blueprint(authentication_blueprint, url_prefix= '/auth')

  return app

