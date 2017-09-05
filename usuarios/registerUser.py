from record import Record
from usuarios.doctorate import Doctorate
from usuarios.graduate import Graduate
from usuarios.manager import Manager
from usuarios.master import Master
from usuarios.researcher import Researcher
from usuarios.teacher import Teacher

class RegisterUser(object):
    
    def __init__(self):
        self.username = input("Usuário: ")
        self.name = input("Nome: ")
        
    def save(self):
        Record().setUser(self.menu()(self.username, self.name))

    def menu(self):
        lista = [Teacher, Manager, Researcher, [Graduate, Master, Doctorate]]
        print("1: {}\n2: {}\n3: {}\n4: {}".format('Professor', 'Administrador', 'Pesquisador', 'Aluno'))
        typeUser = -1 + int(input("Tipo de Usuário: "))
        if typeUser == 3:
            print("1: {}\n2: {}\n3: {}".format('Graduação', 'Mestrado', 'Doutorado'))
            typeUser = -1 + int(input("Tipo de Usuário: "))
            lista[3][typeUser]
        return lista[typeUser]
    