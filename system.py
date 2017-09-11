from record import Record
from users.systemUser import SystemUser
from exceptions import UsernameNotExist

class System(object):
    
    def menu(self):
        print("1: {}\n2: {}\n3: {}".format("User", "Resource", "Activity"))
    
    def register_user(self):
        Record().setUser(SystemUser().registerUser())
        print("User save!")
    
    def consult_user(self):
        print("Consult User\nEnter 0 to exit")
        username = input("Username: ")
        if username == 0:
            pass
        else:
            try:
                return Record().getUser(username)
            except UsernameNotExist:
                print("User not exist!")
                self.consult_user()
    
    def register_resource(self):
        pass

    def consult_resource(self):
        pass

    def change_state(self):
        pass