class Error(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DateInvalid(Error):
    def __init__(self, message):
        super().__init__(message)

class DateStartNone(Error):
    def __init__(self, message):
        super().__init__(message)