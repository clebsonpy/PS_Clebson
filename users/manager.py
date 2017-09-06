from usuarios.user import User

class Manager(User):

    def __init__(self, name, email):
        super().__init__(name, email)

    def allocateResource(self, Resource):
        self.__resource[Resource.identificated] = Resource

    def changeStateResource(self, identificated):
        pass

    def __repr__(self):
        pass