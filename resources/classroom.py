from resource import Resources
from state import EmProcessoAlocacao
from date import DateHour

class Classroom(Resources):

    def __init__(self, identificated, response):
        self.identificated = identificated
        self.__date_hour = DateHour()
        self.response = response
        self.__state = EmProcessoAlocacao()
    
    def change(self, state):
        self.__state.switch(state)
    
    def getState(self):
        return self.__state.name

    def setStart_date(self, start_date):
       self.__date_hour.setStart_date(start_date)
    
    def setEnd_date(self, end_date):
        self.__date_hour.setEnd_date(end_date)

    def getStart_date(self):
       return self.__date_hour.getStart_date()
    
    def getEnd_date(self):
        return self.__date_hour.getEnd_date()