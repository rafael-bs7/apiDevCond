
from models.Unit import Unit

class UnitController():
    
    def __init__(self):
        self.unit_model = Unit()   
        
    def getinfo(self, id):
        result = []
        try:
            res = self.unit_model.get_unit_by_id_ower(id)
            
            for r in res:
                result.append({
                    'id': r.id,
                    'name': r.name,
                    'id_ower':r.id_ower
                })
            
            status = 200
        except Exception as e:
            print(e)
            result = []
            status =400
        finally:
            return {
                'result': result,
                'status': status
            }
            
        return {}
    
    def addPerson():
        return ''
    
    def addVehicle():
        return ''
    
    def addpet():
        return ''
    
    def removePerson():
        return ''
    
    def removeVehicle():
        return ''
    
    def removePet():
        return ''
    
    