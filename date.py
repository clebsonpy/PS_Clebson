import datetime
import pytz
from exceptions import DateInvalid, DateStartNone

class DateHour():
    tz = pytz.timezone('America/Maceio')
    def __init__(self):
        self.date_now = datetime.datetime.now(tz=self.tz)
        self.__start_date = None
        self.__end_date = None

    def setStart_date(self, start_date):
        start_date = datetime.datetime.strptime(start_date + ' -0300', '%d/%m/%Y %H:%M %z')
        if start_date < self.date_now:
            raise DateInvalid('Data e Hora inicio invalida!')
        
        self.__start_date = start_date

    def setEnd_date(self, end_date):
        end_date = datetime.datetime.strptime(end_date + ' -0300', '%d/%m/%Y %H:%M %z')
        if self.__start_date is None:
            raise DateStartNone('Entre com a Data e Hora de Início!')
        elif end_date < self.__start_date:
            raise DateInvalid('Data e Hora inicio invalida!')

        self.__end_date = end_date
    
    def getStart_date(self):
        return self.__start_date

    def getEnd_date(self):
        return self.__end_date