from flask import Flask
from .models import db 

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://messages.db'   

    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
        from . import routes
        app.register_blueprint(routes.bp)
    
    return app