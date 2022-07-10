
from flask import Flask, current_app
from config import Config
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
# CORS(app)

# config file with secret key saved within a class called Config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# importing at the bottom as a workaround to circular imports
# from app import routes should be here
from app import routes, models
