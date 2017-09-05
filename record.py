from exceptions import UsernameNotExist, ResourceNotExist

class Record(object):
    __instance = None
    def __new__(cls):
        if not Record.__instance:
            Record.__instance = super(Record, cls).__new__(cls)
        return Record.__instance

    def __init__(self):
        self.__user = {}
        self.__resource = {}
    
    def getUser(self, username):
        if username in self.__user:
            return self.__user[username]
        else:
            raise UsernameNotExist("User not exist!")
    
    def setUser(self, User):
        self.__user[User.getUsername()] = User
    
    def getResource(self, identificated):
        if identificated in self.__resource:
            return self.__resource[identificated]
        else:
            raise ResourceNotExist("Resource not exist!")