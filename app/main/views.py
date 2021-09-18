from flask import render_template
from . import main
from ..models import User
from flask_login import login_required
from .. import db,photos
import markdown2  


# Views

@main.route('/')
@login_required
def index():


    '''
    View movie page function that returns the movie details page and its data
    
    '''
    

    return render_template('index.html')
