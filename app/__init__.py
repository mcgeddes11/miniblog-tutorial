from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager
from config import basedir
from models import User

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

from app import views, models
