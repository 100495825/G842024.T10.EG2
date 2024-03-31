''' Class HotelManagementException. (GE2.2) '''
class HotelManagementException(Exception):
    def __init__(self, strMessage):
        self.__strMessage = strMessage


    @property
    def message(self):
        return self.__strMessage

    @message.setter
    def message(self, strValue):
        self.__strMessage = strValue

