from abc import ABCMeta, abstractmethod

class RecurseState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Status Alterado")
            self.__class__ = state
        else:
            print("Status não pode ser alterado")

class EmProcessoAlocacao(RecurseState):
    name = "Em processo de alocação"
    allowed = ["Alocado"]

class Alocado(RecurseState):
    name = "Alocado"
    allowed = ["Em andamento"]

class EmAndamento(RecurseState):
    name = "Em andamento"
    allowed = ["Concluído"]

class Concluido(RecurseState):
    name = "Concluído"
    allowed = ["Em processo de alocação"]