from abc import ABCMeta,  abstractmethod

class User(metaclass = ABCMeta):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def __repr__(self):
        pass