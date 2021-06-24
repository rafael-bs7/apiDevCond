from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class  Area(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    allowed = db.Column(db.Integer, default=1,nullable=False)
    title = db.Column(db.String(50),nullable=False)
    cover= db.Column(db.String(50),nullable=False)
    days= db.Column(db.String(100),nullable=False)
    start_time= db.Column(db.Time(), nullable=False)
    end_time= db.Column(db.Time(), nullable=False)
    