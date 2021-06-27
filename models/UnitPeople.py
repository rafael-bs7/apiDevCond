from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Unit import Unit

class  UnitPeople(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    name = db.Column(db.String(100),nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return '%s - %s' % (self.id, self.name)
    
    
    def get_unit_people_by_id_unit(self, id_unit):
        try:
            res = db.session.query(UnitPeople).filter(UnitPeople.id_unit==id_unit).all()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
    
    def addPerson(self, name, birthdate, id):
        try:
            self.name= name
            self.birthdate = birthdate
            self.id_unit = id
            db.session.add(self)
            db.session.commit()
            return True
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return False    