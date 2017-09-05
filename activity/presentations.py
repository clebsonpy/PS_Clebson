from activity import Activity

class Presentations(Activity):

    def __init__(self, title):
        super().__init__(title)
        self.__description = None
        self.__participants = None
        self.__supportMaterial = None
        self.__permission = []

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, participants):
        self.__participants = participants

    @property
    def supportMaterial(self):
        return self.__supportMaterial

    @supportMaterial.setter
    def supportMaterial(self, supportMaterial):
        self.__supportMaterial = supportMaterial