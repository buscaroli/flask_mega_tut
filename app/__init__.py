
from flask import Flask
from config import Config
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

# config file with secret key saved within a class called Config
app.config.from_object(Config)

# importing at the bottom as a workaround to circular imports
# from app import routes should be here
from app import routes
