from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit

class  FoundAndLost(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    status= db.Column(db.String(50),default='LOST',nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    where = db.Column(db.String(50), nullable=False)
    datecreated = db.Column(db.Date(), nullable=False)
    
    def __repr__(self):
        return '%s - %s' % (self.id, self.description)
    
    
    
    def get_all_found_lost(self):
        try:
            res = db.session.query(FoundAndLost).all()
        except Exception as e:
            res =[]
        finally:
            return res

