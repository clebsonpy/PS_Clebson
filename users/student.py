from users.user import User

class Student(User):

    def __init__(self, name, email):
        super().__init__(name, email)
    
    def __repr__(self):
        return "Name: {}\nE-mail: {}".format(self.name, self.email)
