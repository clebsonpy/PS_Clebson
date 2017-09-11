from resources.auditorium import Auditorium
from resources.classroom import Classroom
from resources.laboratory import Laboratory
from resources.projector import Projector


class SystemResource(object):
     __instance = None
    
    def __new__(cls):
        if not RegisterResource.__instance:
            RegisterResource.__instance = super(RegisterResource, cls).__new__(cls)
        
        return RegisterResource.__instance
    
    def __init__(self):
        self.identificated = input("Identificação: ")

    def registerResource(self):
        pass

    def menuRegisterResource(self):
        pass
    
    def menuEditResource(self):
        pass