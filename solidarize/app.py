from flask import Flask
from .config import Config
from .extensions import db, login_manager, bcrypt
from .auth import auth_bp
from .main import main_bp
from .donors import donors_bp
from .campaigns import campaigns_bp
from .donations import donations_bp
from .reports import reports_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(donors_bp, url_prefix="/donors")
    app.register_blueprint(campaigns_bp, url_prefix="/campaigns")
    app.register_blueprint(donations_bp, url_prefix="/donations")
    app.register_blueprint(reports_bp, url_prefix="/reports")

    with app.app_context():
        db.create_all()

    return app

# Dev server
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
