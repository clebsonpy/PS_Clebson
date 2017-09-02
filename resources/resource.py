from abc import ABCMeta, abstractmethod

class Resources(metaclass = ABCMeta):
    
    def __init__(self):
        pass

    @abstractmethod
    def change(self, state):
        pass

    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def setStart_date(self, start_date):
        pass
    
    @abstractmethod
    def setEnd_date(self, end_date):
        pass

    @abstractmethod
    def getStart_date(self):
       pass

    @abstractmethod
    def getEnd_date(self):
        pass