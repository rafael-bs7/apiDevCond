from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit
from models.Area import Area

class  Reservation(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    id_area = db.Column(db.Integer,db.ForeignKey(Area.id), nullable=False)
    reservation_date = db.Column(db.DateTime(), nullable=False)
