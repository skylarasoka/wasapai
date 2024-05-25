# This file initiazes the flask app and sets up configuration and routes.


from flask import Flask
from .models import db 

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://messages.db'   

    #Setup SQLAlchemy with the app
    db.init_app(app)
    
    with app.app_context():
        db.create_all() #Create the database tables
        
        from . import routes
        app.register_blueprint(routes.bp) #Register the routes blueprint with the app
    
    return app