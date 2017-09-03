from resource import Resources
from state import EmProcessoAlocacao
from date import DateHour

class Auditorium(Resources):

    def __init__(self, identificated):
        self.identificated = identificated
        self.__date_hour = DateHour()
        self.__response = None
        self.__state = EmProcessoAlocacao()
    
    @property
    def state(self):
        return self.__state.name
    
    @property
    def start_date(self):
        return self.__date_hour.getStart_date()
    @property
    def end_date(self):
        return self.__date_hour.getEnd_date()
        
    @state.setter
    def state(self, state):
        self.__state.switch(state)
    
    @start_date.setter
    def start_date(self, start_date):
       self.__date_hour.setStart_date(start_date)
    
    @end_date.setter
    def end_date(self, end_date):
        self.__date_hour.setEnd_date(end_date)