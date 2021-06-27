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
    
    def __repr__(self):
        return '%s - %s' % (self.id, self.name)
    
    
    
    def get_unit_pet_by_id_unit(self, id_unit):
        try:
            res = db.session.query(UnitPet).filter(UnitPet.id_unit==id_unit).all()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
    
    def addPets(self, name, race, id):
        try:
            self.name= name
            self.race = race
            self.id_unit = id
            db.session.add(self)
            db.session.commit()
            return True
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return False    