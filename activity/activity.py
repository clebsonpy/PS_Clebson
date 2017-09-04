from abc import ABCMeta, abstractmethod

class Activity(metaclass = ABCMeta):

    def __init__(self, title):
        self.title = title
    
    @abstractmethod
    @property
    def description(self):
        pass

    @abstractmethod
    @description.setter
    def description(self, description):
        pass

    @abstractmethod
    @property
    def participants(self):
        pass

    @abstractmethod
    @participants.setter
    def participants(self, participants):
        pass

    @abstractmethod
    @property
    def supportMaterial(self):
        pass

    @abstractmethod
    @supportMaterial.setter
    def supportMaterial(self, supportMaterial):
        pass