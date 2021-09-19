import os

class Config:

    '''
    
    General configuration parent class
    
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY='nickson00841999code'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitch_flask'




     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

        # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
       

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass



class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitch_test'
    pass


class DevConfig(Config):
    
  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/pitch_flask'
    DEBUG = True



config_options = {

    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig

}    






