from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)

from models.Wall import Wall
from models.User import User

class  WallLike(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_wall = db.Column(db.Integer,db.ForeignKey(Wall.id), nullable=False)
    id_user = db.Column(db.Integer,db.ForeignKey(User.id), nullable=False)
    
    def __repr__(self):
        return '%s' % (self.id)

    
    def get_like(self, id):
       
        try:
            res = db.session.query(func.count('*')).filter(WallLike.id_wall==id).all()
        except Exception as e:
            res = 0
        finally:
            db.session.close()
            return res
    
    def get_liked(self, id_wall, id_user):
        
        try:
            res = db.session.query(WallLike).filter(WallLike.id_user == id_user, WallLike.id_wall== id_wall).first()
        except  Exception as e:
            res = ''
        finally:
            db.session.close()
            return res
    
    def delete(self, id_wall, id_user):
        try:
            db.session.query(WallLike).filter(WallLike.id_wall == id_wall, WallLike.id_user==id_user).delete()
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
    
    def insertLike(self, id_wall, id_user):
        try:
            self.id_user = id_user
            self.id_wall = id_wall
            db.session.add(self)
            db.session.commit()
            
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
            
        
        
        
    
