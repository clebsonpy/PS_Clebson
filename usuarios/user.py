from abc import ABCMeta,  abstractmethod

class User(metaclass = ABCMeta):

    def __init__(self, username, name):
        self.__username = username
        self.__name = name

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getName(self):
        return self.__name

    def setName(self, name):
        self.name = name

    def __repr__(self):
        pass