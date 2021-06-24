from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


from passlib.hash import pbkdf2_sha256


class  Wall(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30),nullable=False)
    body = db.Column(db.String(100), nullable=False)
    datecreated = db.Column(db.DateTime(), nullable=False)
      
    def __repr__(self):
        return '%s - %s' % (self.id, self.title)
    
    def get_wall_by_id(self, id):
        try:
            res = db.session.query(Wall).filter(Wall.id==id).first()

        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
    
    def get_all_wall(self):
        try:
            res = db.session.query(Wall).all()
        except Exception as e:
            res =[]
        finally:
            return res