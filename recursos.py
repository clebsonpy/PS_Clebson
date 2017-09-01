from abc import ABCMeta, abstractmethod

class Recourses (metaclass = ABCMeta):
    def __init__(self, ):
        self.__identificated = None
        self.__startDate = None
        self.__endDate = None
        self.__response = None
        self.__state = statusas
    
    @abstractmethod
    def status(self, status):
        pass

