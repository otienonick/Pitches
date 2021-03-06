from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_login import LoginManager
from flask_simplemde import SimpleMDE



bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()


login_manager = LoginManager()
login_manager.session_protection = 'strong' #provides different security levels.
login_manager.login_view = 'auth.login'


def create_app(config_name):

    # inititalizing application
    app = Flask(__name__)

 
    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)


    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')


    # configure UploadSet
    configure_uploads(app,photos)
    
    return app
