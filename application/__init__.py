from flask import Flask
from config import Config
from flask_mail import Mail



app = Flask(__name__)
mail = Mail(app)
app.config.from_object(Config)

from application import routes