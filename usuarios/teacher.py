from usuarios.user import User
from exceptions import ResourceAlocateError, ResourceChangeStateError
from record import Record

class Teacher(User):

    def __init__(self, username, name):
        super().__init__(username, name)

    def allocateResource(self, Resource, identificated):
        resource = Resource(identificated)
        resource.response()
        Record().__resource[identificated] = Resource(identificated)
    
    def changeStateResource(self, identificated):
        if identificated in Record().__resource:
            pass
        else:
            raise ResourceChangeStateError("Teacher not Resource")

    def __repr__(self):
        pass