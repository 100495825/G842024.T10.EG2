''' Class HotelReservation (GE2.2) '''
import hashlib

import json

from datetime import datetime

class HOTELRESERVATION:
    def __init__(self, strIdCard, strCreditCardNum, strNameAndSurname, strPhoneNumber, strRoomType, intNumDays):
        self.__strCreditCardNum = strCreditCardNum
        self.__strIdCard = strIdCard
        justnow = datetime.utcnow()
        self.__dateArrival = datetime.timestamp(justnow)
        self.__strNameAndSurname = strNameAndSurname
        self.__strPhoneNumber = strPhoneNumber
        self.__strRoomType = strRoomType
        self.__intNumDays = intNumDays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__strIdCard,
                    "name_surname": self.__strNameAndSurname,
                    "credit_card": self.__strCreditCardNum,
                    "phone_number:": self.__strPhoneNumber,
                    "arrival_date": self.__dateArrival,
                    "num_days": self.__intNumDays,
                    "room_type": self.__strRoomType,
                    }
        return "HotelReservation:" + json_info.__str__()
    @property
    def CREDITCARD(self):
        return self.__strCreditCardNum
    @CREDITCARD.setter
    def CREDITCARD(self, strValue):
        self.__strCreditCardNum = strValue

    @property
    def IDCARD(self):
        return self.__strIdCard
    @IDCARD.setter
    def IDCARD(self, strValue):
        self.__strIdCard = strValue


    @property
    def LOCALIZER(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()