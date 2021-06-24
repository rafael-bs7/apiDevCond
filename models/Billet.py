from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit

class  Billet(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    fileurl = db.Column(db.String(120),nullable=False)

