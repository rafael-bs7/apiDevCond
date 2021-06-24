from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class  Doc(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    tile = db.Column(db.String(50),nullable=False)
    file_url= db.Column(db.String(120), nullable=False)


