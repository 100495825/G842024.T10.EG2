''' Class HotelManagement (GE2.2) '''
 class HOTELMANAGMENT( Exception ):
    def __init__( self, strMessage ):
        self.__strMessage = strMessage
        super( ).__init__( self.strMessage )

    @property
    def MESSAGE( self ):
        return self.__strMessage

    @MESSAGE.setter
    def MESSAGE( self, strValue ):
        self.__strMessage = strValue

