from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit

class  UnitVehicles(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    title = db.Column(db.String(100),nullable=False)
    color = db.Column(db.String(20),nullable=False)
    plate = db.Column(db.String(20),nullable=False)

