
from models.Unit import Unit
from models.UnitPeople import UnitPeople
from models.UnitVehicles import UnitVehicles
from models.UnitPet import UnitPet

class UnitController():
    
    def __init__(self):
        self.unit_model = Unit()  
        self.unit_peoples_model = UnitPeople()
        self.unit_vehicles_model = UnitVehicles()
        self.unit_pets_model = UnitPet() 
        
    
    
    def getInfo (self, id):
        res = self.unit_model.get_unit_by_id(id)
        if res:
            return True
        else:
            return False
    
    def getPeople(self, id_unit):
        result = []
        try:
            res = self.unit_peoples_model.get_unit_people_by_id_unit(id_unit)
            
            for r in res:
                result.append({
                    'id': r.id,
                    'name': r.name,
                    'birthdate':r.birthdate.strftime("%d/%m/%Y"),
                })
            
        except Exception as e:
            print(e)
            result = []
        finally:
            return result
        

    def getVehicles(self, id_unit):
        
        result = []
        try:
            res = self.unit_vehicles_model.get_unit_vehicle_by_id_unit(id_unit)
            
            for r in res:
                result.append({
                    'id': r.id,
                    'title': r.title,
                    'color':r.color,
                    'plate': r.plate
                })
            
        except Exception as e:
            print(e)
            result = []
        finally:
            return result
        

    
    def getPets(self, id_unit):
              
        result = []
        try:
            res = self.unit_pets_model.get_unit_pet_by_id_unit(id_unit)
            for r in res:
                result.append({
                    'id': r.id,
                    'name': r.name,
                    'race':r.race
                })
            
        except Exception as e:
            print(e)
            result = []
        finally:
            return result
         
        

    
    #descartar
    def getinfo(self, id):
        result = []
        try:
            res = self.unit_model.get_unit_by_id(id)
            
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
            
    
    def add_Person(self, name, birthdate, id):
        try:
            res = self.unit_peoples_model.addPerson(name, birthdate,id)
            return res
        except Exception as e:
            print (e)
            return ''
    
    def add_Vehicle(self, title, color, plate, id):
        try:
            res = self.unit_vehicles_model.addVehicle(title, color, plate,id)
            return res
        except Exception as e:
            print (e)
            return ''
    
    def add_Pet(self, name, race, id):
        try:
            res = self.unit_pets_model.addPets(name, race, id)
            return res
        except Exception as e:
            print (e)
            return ''
    
    def removePerson():
        return ''
    
    def removeVehicle():
        return ''
    
    def removePet():
        return ''
    
    