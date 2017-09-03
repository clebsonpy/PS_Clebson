from abc import ABCMeta, abstractmethod

class Resources(metaclass = ABCMeta):
    
    def __init__(self):
        pass

    @abstractmethod
    @property
    def state(self):
        pass

    @abstractmethod
    @property
    def start_date(self):
       pass

    @abstractmethod
    @property
    def end_date(self):
        pass

    @abstractmethod
    @state.setter
    def state(self, state):
        pass

    @abstractmethod
    @start_date.setter
    def start_date(self, start_date):
        pass
    
    @abstractmethod
    @end_date.setter
    def end_date(self, end_date):
        pass