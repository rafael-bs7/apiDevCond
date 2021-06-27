# -*- coding: utf-8 -*-
from flask import Flask, Response, json, request, jsonify, abort, render_template
# config import
from config import app_config, app_active
config = app_config[app_active]


from flask_sqlalchemy import SQLAlchemy
from functools import wraps

from controller.AuthController import AuthController
from controller.UnitController import UnitController
from controller.WallController import WallController
from controller.FoundAndLostController import FoundAndLostController
from models.User  import User

from models.Unit import Unit

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)
    
    def auth_token_required(f):
        @wraps(f)
        def verify_token(*args, **kwargs):
            auth = AuthController()
            try:
                result = auth.verify_auth_token(request.headers['access_token'])
                if result['status'] == 200:
                    return f(*args, **kwargs)
                else:
                    abort(result['status'], result['message'])
            except KeyError as e:
                abort(401, 'Você precisa enviar um token de acesso')

        return verify_token





    @app.route('/')
    def index():
        return 'Hello World!'
    

    @app.route('/auth/register', methods=['POST'])
    def register():
        response={'error':''}
        
        
        if request.form['password'] == request.form['password_confirm']:
            auth = AuthController()
            result = auth.save_user(request.form)
            property ={}
                
            if result:
                user = User() 
                unit = UnitController()
                
                us = user.get_user_by_cpf(request.form['cpf'])
                property = unit.getinfo(us.id)
                
                res = auth.generate_auth_token(request.form['name'], us.id)
                
                message = "Usuário cadastrado com sucesso!"
                
                return {'error': message, 'token': res, 'user':{
                    'id': us.id,
                    'name': us.name,
                    'email': us.email,
                    'cpf': us.cpf
                    }, "properties": property }

            else:
                message = "E-mail ou cpf já cadastrados!"
                return {'error': message}
        else:
            return {'error': 'As senhas devem ser iguais!'}
        
        
    @app.route('/auth/login', methods=['POST'])
    def login():
        
        if request.form['cpf']=='' or request.form['password']=='':
            result= 'Todos os dados devem ser inseridos!'
            return {'error': result}
        else:
            auth = AuthController()
            result = auth.login(request.form['cpf'], request.form['password'])
            
            if result==False:
                mensage = 'Dados inválidos!'
                res=''
                return {'error': mensage}
            else:
                unit = UnitController()
                res = auth.generate_auth_token(result.name, result.id)
                property = unit.getinfo(result.id)  
                return {'error': '', 'token': res, 'user':{
                        'id': result.id,
                        'name': result.name,
                        'email': result.email,
                        'cpf': result.cpf
                    }, "properties": property }

        
    @app.route('/auth/token', methods=['GET'])
    def validateToken():
        auth = AuthController()
        response = auth.verify_auth_token(request.form['token'])
        
        
        if response:
            user = User()
            us = user.get_user_by_id(response['id'])
            
            unit = UnitController()
            property = unit.getinfo(us.id)  
            
            return {'error': '', 'user':{
                    'id': us.id,
                    'name': us.name,
                    'email': us.email,
                    'cpf': us.cpf
                }, "properties": property }
        else:
            return {'error':'Não autorizado!' }
        
    
    @app.route('/walls')
    def get_walls():
        
        wall = WallController()
        res = wall.getWall()
        
        auth = AuthController()
        response = auth.verify_auth_token(request.form['token'])
        
        vetor ={}
        result =[]
        
        for r in res:
            like = wall.getLikes(r['id'])
            liked = wall.getLiked(r['id'],response['id'])
        
            if liked:
                var = True
            else:
                var=False

            vetor = r
            vetor.update({'likes':like[0][0], 'liked': var})
            result.append(vetor)

        return {
            'error':'',
            'list': result 
        }
    
    @app.route('/wall/<int:id>/like', methods=['POST'])
    def like(id):
        wall = WallController()    
        auth = AuthController()
        response = auth.verify_auth_token(request.form['token'])
        
        melikes = wall.getLiked(id,response['id'])
        
        if melikes:
            res = wall.deleteLiked(id, response['id'])
            status = False
        else:
            res = wall.setLiked(id, response['id'])
            status= True
        
        likes = wall.getLikes(id)
        
        return {
            'error':'',
            'liked': status,
            'likes': likes[0][0]
        }
    



    @app.route('/foundandlost', methods=['GET', 'POST'])
    def get_found_lost():
        lostFound = FoundAndLostController()
        
        if request.methods == 'GET':
            res = lostFound.getAll()
            return  {'error':'',
                'lost': res[0],
                'recovered':res[1]
                }
        else:
            res = lostFound.insert()
            return ''
        
    @app.route('/unit/<int:id>', methods=['GET'])
    def getInfo(id):
        unit = UnitController()
        res = unit.getInfo(id)
        
        if res:
           peoples = unit.getPeople(id)
           vehicles = unit.getVehicles(id)
           pets = unit.getPets(id)
           return {
                'error': '',
                'peoples': peoples,
                'vehicles': vehicles,
                'pets': pets
            }
        else:
            return {
                'error': 'Propriedade não existente',
            }
        
    
    @app.route('/unit/<int:id>/addperson', methods=['POST'])
    def addperson(id):
        name = request.form['name']
        birthdate = request.form['birthdate']
        
        if name == '' or birthdate == '':
            message = 'Preencha todos os campos!'
        else:
            unit = UnitController()
            res = unit.add_Person(name, birthdate, id)
            if res:
                message = 'Cadastro realizado com sucesso'
            else:
                message = 'Erro ao efetivar o cadastro!'

        return {'error': message}
    
    @app.route('/unit/<int:id>/addvehicle', methods=['POST'])
    def addvehicle(id):
        title = request.form['title']
        color = request.form['color']
        plate = request.form['plate']
        
        if title == '' or color == '' or plate == '':
            message = 'Preencha todos os campos!'
        else:
            unit = UnitController()
            res = unit.add_Vehicle(title, color,plate, id)
            if res:
                message = 'Cadastro realizado com sucesso'
            else:
                message = 'Erro ao efetivar o cadastro!'

        return {'error': message}
            
    
    @app.route('/unit/<int:id>/addpet', methods=['POST'])
    def addpet(id):
        name = request.form['name']
        race = request.form['race']

        
        if name == '' or race == '':
            message = 'Preencha todos os campos!'
        else:
            unit = UnitController()
            res = unit.add_Pet(name, race, id)
            if res:
                message = 'Cadastro realizado com sucesso'
            else:
                message = 'Erro ao efetivar o cadastro!'

        return {'error': message}

    # rota temporária
    @app.route('/units')
    def get_units():
        unit = Unit()
        res = unit.get_unit_by_id_ower(request.form['id'])
        print(res)
        return {
            'id': res.id,
            'name': res.name,
            'id_ower': res.id_ower
        }
        
    return app