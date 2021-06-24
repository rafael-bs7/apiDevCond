from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class  Unit(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    id_ower= db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '%s - %s' % (self.id, self.name)
    
    def get_unit_by_id_ower(self, id_ower):
        try:
            res = db.session.query(Unit).filter(Unit.id_ower==id_ower).first()
            print('deu certo')
        except Exception as e:
            res = None
        finally:
            db.session.close()
            return res