from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pfv2.config import Config
# from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    
    # from .models import Account, Category, Budget, Incoming, Expense 
    # from .models import Account, AccountType, Budget
    from pfv2.models import Account, AccountType, Budget

    # Blueprint for generic views in our app
    # from .main import views as views_blueprint
    from pfv2.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Blueprint for admin view our app
    #from .admin import admin as admin_blueprint
    from pfv2.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
   
    #print(app.url_map)  

    return app
