from record import Record
from users.registerUser import RegisterUser
from exceptions import UsernameNotExist

class System(object):
    
    def register_user(self):
        Record().setUser(RegisterUser().user())
        print("User save!")
    
    def consult_user(self):
        print("Consult User")
        username = input("Username: ")
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