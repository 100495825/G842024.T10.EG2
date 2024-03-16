
import hashlib

import json

from datetime import datetime

class HOTELRESERVATION:
    def __init__( self, strIdCard, strCreditCardNum, strNameAndSurname, strPhoneNumber, strRoomTyoe, intNumDays ):
        self.__strCreditCardNum = strCreditCardNum
        self.__strIdCard = strIdCard
        justnow = datetime.utcnow()
        self.__ARRIVAL = datetime.timestamp(justnow)
        self.__strNameAndSurname = strNameAndSurname
        self.__strPhoneNumber = strPhoneNumber
        self.__strRoomTyoe = strRoomTyoe
        self.__intNumDays = intNumDays

    def __str__( self ):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + json_info.__str__()
    @property
    def CREDITCARD(self):
        return self.__crEDITcardnumber
    @CREDITCARD.setter
    def CREDITCARD(self, value):
        self.__crEDITcardnumber = value

    @property
    def IDCARD(self):
        return self.__idcard
    @IDCARD.setter
    def IDCARD(self, value):
        self.__idcard = value


    @property
    def LOCALIZER( self ):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()