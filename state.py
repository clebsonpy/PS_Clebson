from abc import ABCMeta, abstractmethod

class RecurseState():
    name = "state"
    stateActual = []
    response = []
    
    @abstractmethod
    def status(self, state):
        if state.name in self.response:
            print("Status Alterado")
            self.__class__ = state
        else:
            print("Status não pode ser alterado")

class EmProcessoAlocacao(RecurseState):
    name = "Em processo de alocação"
    response = []