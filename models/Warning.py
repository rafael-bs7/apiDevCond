from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class  Warning(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    status= db.Column(db.String(50),default='IN_REVIEW',nullable=False)
    datecreated = db.Column(db.Date(), nullable=False)
    photos = db.Column(db.Text(), nullable=False)
