from flask import Flask

app = Flask(__name__)

# importing at the bottom as a workaround to circular imports
from app import routes
