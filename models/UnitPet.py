from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit

class  UnitPet(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    name = db.Column(db.String(100),nullable=False)
    race = db.Column(db.String(20),nullable=False)
    
   