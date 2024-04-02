''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib

class HOTELSTAY():
    def __init__(self, strIdCard, strLocalizer, intNumDays, strRoomType):
        self.__strAlg = "SHA-256"
        self.__strRoomType = strRoomType
        self.__strIdCard = strIdCard
        self.__strLocalizer = strLocalizer
        dateJustNow = datetime.utcnow( )
        self.__dateArrival = dateJustNow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.__dateDeparture = self.__dateArrival + (intNumDays * 24 * 60 * 60)
        self.strRoomKey = hashlib.sha256(self.__SIGNATURESTRING().encode()).hexdigest()

    def __SIGNATURESTRING(self):
        """Composes the string to be used for generating the key for the room"""
        return "{ alg:"+self.__strAlg+",typ:"+self.__strRoomType+",localizer:"+\
            self.__strLocalizer+",arrival:"+self.__dateArrival+\
            ",departure:"+self.__dateDeparture+" }"

    @property
    def IDCARD(self):
        """Property that represents the product_id of the patient"""
        return self.__strIdCard

    @IDCARD.setter
    def IDCARD(self, strValue):
        self.__strIdCard = strValue

    @property
    def LOCALIZER(self):
        """Property that represents the order_id"""
        return self.__strLocalizer

    @LOCALIZER.setter
    def LOCALIZER(self, strValue):
        self.__strLocalizer = strValue

    @property
    def ARRIVAL(self):
        """Property that represents the phone number of the client"""
        return self.__dateArrival

    @property
    def ROOMKEY(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__SIGNATURESTRING.encode()).hexdigest()

    @property
    def DEPARTURE(self):
        """Returns the issued at value"""
        return self.__dateDeparture

    @DEPARTURE.setter
    def DEPARTURE(self, strValue):
        self.__dateDeparture = strValue