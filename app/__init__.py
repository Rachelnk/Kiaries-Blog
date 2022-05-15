from ensurepip import bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)
  
  # initializing flask extensions
  db.init_app(app)
  bootstrap.init_app(app)

  # Creating the app configurations
  app.config.from_object(config_options[config_name])
  # Registering the blueprint
  from .main import main as main_blueprint
  from .auth import auth as authentication_blueprint
  app.register_blueprint(main_blueprint)
  app.register_blueprint(authentication_blueprint, url_prefix= '/auth')

  return app

