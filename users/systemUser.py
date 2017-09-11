from users.doctorate import Doctorate
from users.graduate import Graduate
from users.manager import Manager
from users.master import Master
from users.researcher import Researcher
from users.teacher import Teacher

class SystemUser(object):
    __instance = None
    
    def __new__(cls):
        if not SystemUser.__instance:
            SystemUser.__instance = super(SystemUser, cls).__new__(cls)
        
        return SystemUser.__instance
    
    def __init__(self):
        print("1: {}\n2: {}\n3: {}".format('Register User', 'Edit User', 'Delete User'))
        self.option = int(input("Enter the desired option: "))
        if self.option == 1:
            self.registerUser()
        elif self.option == 2:
            self.editUser()
        elif self.option == 3:
            self.deleteUser()

    def registerUser(self):
        x = self.menuRegisterUser()
        user = eval(x+'("%s", "%s")' % (self.username, self.name))
        return user

    def editUser(self):
        pass
    
    def deleteUser(self):
        pass

    def menuRegisterUser(self):
        lista = ['Teacher', 'Manager', 'Researcher', ['Graduate', 'Master', 'Doctorate']]
        print("1: {}\n2: {}\n3: {}\n4: {}".format('Professor', 'Administrador', 'Pesquisador', 'Aluno'))
        typeUser = -1 + int(input("Tipo de Usuário: "))
        user = lista[typeUser]
        if typeUser == 3:
            print("1: {}\n2: {}\n3: {}".format('Graduação', 'Mestrado', 'Doutorado'))
            typeUser = -1 + int(input("Tipo de Usuário: "))
            user = lista[3][typeUser]
        return user

    def menuEditUser(self):
        print("1: {}\n2: {}".format('Username', 'Name'))
        self.option = int(input("Enter the desired option: "))
        