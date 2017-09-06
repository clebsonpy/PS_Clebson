from usuarios.student import Student

class Master(Student):

    def __init__(self, name, email):
        super().__init__(name, email)