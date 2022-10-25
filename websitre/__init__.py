from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    from .models import User, Note
    from .views import views
    from .auth import auth, sign_up
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sdsa4213v>321s%**3ffggs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/bobdb'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
