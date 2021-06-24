from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


from passlib.hash import pbkdf2_sha256

class  User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(13), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return '%s - %s' % (self.id, self.name)
    
    def save(self):
       
        try:
            pas = self.hash_password(self.password)
            self.password= pas
            db.session.add(self)
            db.session.commit()
            return True
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    
 

    def get_user_by_email(self,email):
        try:
            res = db.session.query(User).filter(User.email==email).first()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
        
    def get_user_by_id(self,id):
        try:
            res = db.session.query(User).filter(User.id==id).first()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
        
    

    def get_user_by_cpf(self,cpf):
        try:
            res = db.session.query(User).filter(User.cpf==cpf).first()
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res
    
    
    def hash_password(self, password):
        try:
            return pbkdf2_sha256.hash(password)
        except Exception as e:
            print("Erro ao criptografar senha %s" % e)

    
    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    
    def verify_password(self, password_no_hash, password_database):
        try:
            return pbkdf2_sha256.verify(password_no_hash, password_database)
        except ValueError:
            return False