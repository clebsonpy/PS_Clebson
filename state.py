from abc import ABCMeta, abstractmethod
from usuarios import Professor(), Adminstardor(), Pesquisador()

class RecurseState():
    name = "state"
    stateActual = None
    responses = []

    @abstractmethod
    def status(self, state, response):
        if response in self.responses:
            print("Status Alterado")
            self.__class__ = state
        else:
            print("Status não pode ser alterado")

class EmProcessoAlocacao(RecurseState):
    name = "Em processo de alocação"
    stateActual = None
    response = [Professor(), Adminstardor(), Pesquisador()]