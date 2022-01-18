class AttributeInitType(type):
    def __call__(self,*args,**kwargs):
        obj = type.__call__(self,*args)
        for name, value in kwargs.items():
            setattr(obj,name,value)
        return obj
    
class Submarine(object, metaclass = AttributeInitType):
    my_attrs = ['color','year','name']
    
class Tank(object,metaclass = AttributeInitType):
    my_attrs = ['weight','year','identifier']
    
sub = Submarine(name = "Narwal", year = 2000, color ="Black")
tank = Tank(weight = 5000,year=1956,identifier = "AXXXXXXXX123")

print(tank.identifier)
