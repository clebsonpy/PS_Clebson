class Error(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DateInvalidError(Error):
    pass

class DateStartNoneError(Error):
    pass

class ResourceAlocateError(Error):
    pass

class ResourceChangeStateError(Error):
    pass

class PermissionError(Error):
    pass

class UsernameNotExist(Error):
    pass

class ResourceNotExist(Error):
    pass