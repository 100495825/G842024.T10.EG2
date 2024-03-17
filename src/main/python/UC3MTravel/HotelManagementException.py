''' Class HotelManagementException. (GE2.2) '''
class HOTELMANAGEMENTEXCEPTION(Exception):
    def __init__(self, strMessage):
        self.__strMessage = strMessage
        super( .__init__(self.__strMessage)

    @property
    def MESSAGE(self):
        return self.__strMessage

    @MESSAGE.setter
    def MESSAGE(self, strValue):
        self.__strMessage = strValue

