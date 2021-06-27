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

    def __repr__(self):
        return '%s - %s' % (self.id, self.title)
    
    
    
    def get_unit_vehicle_by_id_unit(self, id_unit):
        try:
            res = db.session.query(UnitVehicles).filter(UnitVehicles.id_unit==id_unit).all()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
    
    def addVehicle(self, title, color, plate, id):
        try:
            self.title= title
            self.color = color
            self.plate = plate
            self.id_unit = id
            db.session.add(self)
            db.session.commit()
            return True
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return False    