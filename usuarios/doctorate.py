from usuarios.student import Student

class Doctorate(Student):
    
    def __init__(self, name, email):
        super().__init__(name, email)