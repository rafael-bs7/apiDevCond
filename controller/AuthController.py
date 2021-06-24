from flask import Flask, jsonify, request,json
import jwt
from models.User import User
from config import app_config, app_active
config = app_config[app_active]


class AuthController():
    def __init__(self):
        self.user_model = User()        
    
    
    def unauthorized(self):
        return jsonify([{'error':'Não autorizado'},401])
    
    def login(self, cpf, password):
        # verifica se o usuário existe no banco de dados:
        result = self.user_model.get_user_by_cpf(cpf)
        if result is not None:
            res = self.user_model.verify_password(password, result.password)
            
            if res:
                return result
            else:
                return False
        return False
    
    
    def save_user(self, request):
        if (request['name'] == '') or (request['password']=='') or (request['cpf']=='') or (request['email']==''):
            erro = 'Favor preencher todos os campos'
            array = [{'error':erro}]
            return jsonify(array)
        else:
            self.user_model.name = request['name']
            self.user_model.email = request['email']
            self.user_model.password = request['password']
            self.user_model.cpf = request['cpf']
            
        
        return self.user_model.save()
    
    
    def verify_auth_token(self, access_token):
        try:
            return jwt.decode(access_token, config.SECRET, algorithms=['HS256'])
           
        except:
            return ''
    
    def generate_auth_token(self, name, id):
        dict_jwt = {
            'id': id,
            'username': name
        }
        access_token = jwt.encode(dict_jwt, config.SECRET, algorithm='HS256')
        return access_token
    
    
    
    def logout (self):
        return
    
    