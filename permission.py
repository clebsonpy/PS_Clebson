from usuarios.doctorate import Doctorate
from usuarios.graduate import Graduate
from usuarios.manager import Manager
from usuarios.master import Master
from usuarios.researcher import Researcher
from usuarios.teacher import Teacher

class PermissionActivaty(object):

    def traditionalClassroom(self):
        return Teacher

    def presentations(self):
        return Manager, Researcher, Teacher

    def laboratoty(self):
        return Manager, Researcher, Teacher

class PermissionResource(object):

    def allocation(self):
        return Teacher, Researcher, Manager

    def changeState(self):
        return Manager