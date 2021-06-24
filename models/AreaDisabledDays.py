from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Area import Area


class  AreaDisabledDay(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_areas = db.Column(db.Integer, db.ForeignKey(Area.id), nullable=False)
    day = db.Column(db.Integer, nullable=False)


