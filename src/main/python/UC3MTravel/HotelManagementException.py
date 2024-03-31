''' Class HotelManagementException. (GE2.2) '''
class HotelManagementException(Exception):
    def __init__(self, strMessage):
        self.__strMessage = strMessage


    @property
    def MESSAGE(self):
        return self.__strMessage

    @MESSAGE.setter
    def MESSAGE(self, strValue):
        self.__strMessage = strValue

