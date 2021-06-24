from flask import Flask
from config import app_config, app_active
config = app_config[app_active]

from models.User import User
from models.Wall import Wall
from models.WallLike import WallLike

class WallController():   
    def __init__(self):
        self.wall_model = Wall()
        self.wall_like_model = WallLike()   


    def getWall(self):
        result = []
       
        try:
            res = self.wall_model.get_all_wall()     
            for r in res:
                result.append({
                    'id': r.id,
                    'title':r.title,
                    'body':r.body,
                    'datecreated': r.datecreated      
                })
        except Exception as e:
            print('')
        finally:
            return result 
       
    
    def getLikes(self, id):
        try:
            res = self.wall_like_model.get_like(id)
        except Exception as e:
            res = 0
            print(e)
        finally:
            return res
    
    def getLiked(self, id_wall, id_user):
        try: 
            res  = self.wall_like_model.get_liked(id_wall, id_user)
        except Exception as e:
            res = False
            print(e)
        finally:
            return res
        
    def deleteLiked(self, id_wall, id_user):
        try:
            res = self.wall_like_model.delete(id_wall, id_user)
        except Exception as e:
            print(e)
        finally:
            return ''
    
    
    def setLiked(self, id_wall, id_user):
        try:
            res = self.wall_like_model.insertLike(id_wall, id_user)
        except Exception as e:
            print(e)
        finally:
            return ''