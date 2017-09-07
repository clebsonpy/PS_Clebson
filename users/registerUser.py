from users.doctorate import Doctorate
from users.graduate import Graduate
from users.manager import Manager
from users.master import Master
from users.researcher import Researcher
from users.teacher import Teacher

class RegisterUser(object):
    __instance = None
    
    def __new__(cls):
        if not RegisterUser.__instance:
            RegisterUser.__instance = super(RegisterUser, cls).__new__(cls)
        
        return RegisterUser.__instance
    
    def __init__(self):
        self.username = input("Usuário: ")
        self.name = input("Nome: ")
        
    def user(self):
        x = self.menu()
        user = eval(x+'("%s", "%s")' % (self.username, self.name))
        return user

    def menu(self):
        lista = ['Teacher', 'Manager', 'Researcher', ['Graduate', 'Master', 'Doctorate']]
        print("1: {}\n2: {}\n3: {}\n4: {}".format('Professor', 'Administrador', 'Pesquisador', 'Aluno'))
        typeUser = -1 + int(input("Tipo de Usuário: "))
        user = lista[typeUser]
        if typeUser == 3:
            print("1: {}\n2: {}\n3: {}".format('Graduação', 'Mestrado', 'Doutorado'))
            typeUser = -1 + int(input("Tipo de Usuário: "))
            user = lista[3][typeUser]
        return user