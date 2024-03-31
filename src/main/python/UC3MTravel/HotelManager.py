''' Class HotelManager (GE2.2) '''

import json

from .HotelManagementException import HOTELMANAGEMENTEXCEPTION

from .HotelReservation import HOTELRESERVATION
from pathlib import Path


class HOTELMANAGER:
    """Class HotelManager"""
    def __init__(self):
        pass

    def VALIDATENAMESURNAME(self, strNameAndSurname) -> bool:
        if (len(strNameAndSurname) <= 10) or (len(strNameAndSurname) >= 50):
            return False

        for char in strNameAndSurname:
            if char in '1234567890':
                return False

        if ' ' not in strNameAndSurname:
            return False

    def VALIDATECREDITCARD(self, strCreditCardNum:str) ->bool:
            #Comprobar la longitud de la tarjeta de credito
        if len(strCreditCardNum) != 16:
            return False
        intChecksum = int(strCreditCardNum[-1])
        #Metemos los numeros en una lista
        lstNumeros = [int(intNum) for intNum in strCreditCardNum[:-1]]

        # Duplicamos los numeros en las posiciones pares empezando por 1
        lstNumeros = [lstNumeros[i] * 2 if i % 2 == 0 else lstNumeros[i] for i in range(len(lstNumeros))]

        # Sumamos los digitos de los numeros mayores a 9
        lstNumeros = [sum([int(num) for num in str(lstNumeros[i])]) if lstNumeros[i] > 9 else lstNumeros[i] for i in
                   range(len(lstNumeros))]

        # Sumamos todos los numeros y calculamos el checksum teorico
        intSuma = sum(lstNumeros)
        intChecksumTeorica = intSuma * 9 % 10

        return intChecksum == intChecksumTeorica

    def VALIDATE_PHONE_NUMBER(self, strPhoneNumber: str) -> bool:
        if len(strPhoneNumber) != 9:
            return False
        intList = [int(intNum) for intNum in strPhoneNumber]
        for i in intList:
            if i not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
                print(intList)
                return False
        return True

    def VALIDATE_DAYS(self, intDays) -> bool:
        if type(intDays) == str:
            return False
        if 0 < intDays < 11:
            return True
        return False
    def VALIDATE_ID(self, id):
        """Devuelve True si el id entregado es válido, sino False"""
        intId = id[:-1]
        if not isinstance(id, str) or len(id) != 9:
            return False
        try:
            int(intId)
        except ValueError:
            return False
        strLetras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        intIndex = int(intId) % 23
        return id[-1].upper == strLetras[intIndex]
    def VALIDATE_ROOM(self, strRoom):
        """Devuelve True si el tipo de habitación es válido, sino False"""
        if not isinstance(strRoom, str):
            return False
        if strRoom.lower not in ("single", "double", "suite"):
            return False
        return True
    def REGISTER_RESERVATION(self, strCreditCard, strId_Card, strNameSurname, strPhoneNumber, strRoomType, intNumDays):
        if not self.VALIDATECREDITCARD(strCreditCard):
            raise HOTELMANAGEMENTEXCEPTION("Creditcard not valid")
        if not self.VALIDATE_ID(strId_Card):
            raise HOTELMANAGEMENTEXCEPTION("ID not valid")
        if not self.VALIDATENAMESURNAME(strNameSurname):
            raise HOTELMANAGEMENTEXCEPTION("Name not valid")
        if not self.VALIDATE_PHONE_NUMBER(strPhoneNumber):
            raise HOTELMANAGEMENTEXCEPTION("Phone number not valid")
        if not self.VALIDATE_ROOM(strRoomType):
            raise HOTELMANAGEMENTEXCEPTION("Room type not valid")
        if not self.VALIDATE_DAYS(intNumDays):
            raise HOTELMANAGEMENTEXCEPTION("Number of days not valid")
        file_store = str(Path.home())
        file_store += "/PycharmProjects/G842024.T10.EG2/src/JSONfiles/storeReserves.json"
        my_management = HOTELRESERVATION(strId_Card, strCreditCard, strNameSurname, strPhoneNumber, strRoomType,
                                         intNumDays)
        try:
            # Opens the json file and load the data to a list
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found, so init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            # There is an error decoding the JSON file
            raise HOTELMANAGEMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from ex

        # Adds the order to the list
        data_list.append(my_management.__str__())

        try:
            # Opens again the json file and puts all the data in it
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HOTELMANAGEMENTEXCEPTION("Wrong file or file path") from ex

        return my_management.LOCALIZER
    def READDATAFROMJSON(self, strFi):

        try:
            with open(strFi) as f:
                strData = json.load(f)
        except FileNotFoundError as e:
            raise HOTELMANAGEMENTEXCEPTION("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HOTELMANAGEMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from e

        try:
            strC = strData["CreditCard"]
            strP = strData["phoneNumber"]
            req = HOTELRESERVATION(strIdCard="12345678Z", strCreditCardNum=strC, strNameAndSurname="John Doe",
                                    strPhoneNumber=strP, strRoomType="single", intNumDays=3)
        except KeyError as e:
            raise HOTELMANAGEMENTEXCEPTION("JSON Decode Error - Invalid JSON Key") from e
        if not self.VALIDATECREDITCARD(strC): raise HOTELMANAGEMENTEXCEPTION("Invalid credit card number")

        # Close the file
        return req
    #No se si lo siguiente está correcto
