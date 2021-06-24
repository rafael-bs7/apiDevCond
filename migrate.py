from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import app_active, app_config


config = app_config[app_active]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class  User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(13), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class  Unit(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    id_ower= db.Column(db.Integer, nullable=False)


class  UnitPeople(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    name = db.Column(db.String(100),nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

class  UnitVehicles(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    title = db.Column(db.String(100),nullable=False)
    color = db.Column(db.String(20),nullable=False)
    plate = db.Column(db.String(20),nullable=False)
    
class  UnitPet(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    name = db.Column(db.String(100),nullable=False)
    race = db.Column(db.String(20),nullable=False)
    
class  Wall(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30),nullable=False)
    body = db.Column(db.String(100), nullable=False)
    datecreated = db.Column(db.DateTime(), nullable=False)


class  WallLike(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_wall = db.Column(db.Integer,db.ForeignKey(Wall.id), nullable=False)
    id_user = db.Column(db.Integer,db.ForeignKey(User.id), nullable=False)

class  Doc(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    tile = db.Column(db.String(50),nullable=False)
    file_url= db.Column(db.String(120), nullable=False)  

class  Billet(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    fileurl = db.Column(db.String(120),nullable=False)

 
class  Warning(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    status= db.Column(db.String(50),default='IN_REVIEW',nullable=False)
    datecreated = db.Column(db.Date(), nullable=False)
    photos = db.Column(db.Text(), nullable=False)

class  FoundAndLost(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    status= db.Column(db.String(50),default='LOST',nullable=False)
    photo = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    where = db.Column(db.String(50), nullable=False)
    datecreated = db.Column(db.Date(), nullable=False)

class  Area(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    allowed = db.Column(db.Integer, default=1,nullable=False)
    title = db.Column(db.String(50),nullable=False)
    cover= db.Column(db.String(50),nullable=False)
    days= db.Column(db.String(100),nullable=False)
    start_time= db.Column(db.Time(), nullable=False)
    end_time= db.Column(db.Time(), nullable=False)
    

class  AreaDisabledDay(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_areas = db.Column(db.Integer, db.ForeignKey(Area.id), nullable=False)
    day = db.Column(db.Integer, nullable=False)

class  Reservation(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    id_unit = db.Column(db.Integer,db.ForeignKey(Unit.id), nullable=False)
    id_area = db.Column(db.Integer,db.ForeignKey(Area.id), nullable=False)
    reservation_date = db.Column(db.DateTime(), nullable=False)



if __name__ == '__main__':
    manager.run()


    
   
