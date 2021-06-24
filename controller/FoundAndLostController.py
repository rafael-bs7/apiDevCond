
from flask import Flask
from config import app_config, app_active
config = app_config[app_active]

from models.FoundAndLost import FoundAndLost

class FoundAndLostController():
    def __init__(self):
        self.found_lost = FoundAndLost()
    
    
    def getAll(self):
        lost =[]
        recovered =[]
        try:
            res = self.found_lost.get_all_found_lost()
            for r in res:
                
                if r.status == 'LOST':
                    lost.append({
                        'id': r.id,
                        'status':r.status,
                        'photo':r.photo,
                        'description': r.description,
                        'where': r.where,
                        'datecreated': r.datecreated.strftime("%d/%m/%Y")      
                    })
                elif r.status == 'RECOVERED':
                    recovered.append({
                        'id': r.id,
                        'status':r.status,
                        'photo':r.photo,
                        'description': r.description,
                        'where': r.where,
                        'datecreated': r.datecreated.strftime("%d/%m/%Y")      
                    })
           
            result = [lost, recovered]
        except Exception as e:
            print('')
        finally:
            return result 
     
    def insert():
        return ''
    
    def update():
        return ''
    
    