class HOTELMANAGMENT(Exception):
    def __init__(self, strMessage):
        self.__message = strMessage
        super().__init__(self.strMessage)

    @property
    def MESSAGE(self):
        return self.__message

    @MESSAGE.setter
    def MESSAGE(self, strValue):
        self.__message = strValue

