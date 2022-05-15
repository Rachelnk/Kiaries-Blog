import os
class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '123rnk'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kiarie:rayray@localhost/watchlist'

    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
        
 
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }