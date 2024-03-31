''' Class HotelManager (GE2.2) '''

import json

from .HotelManagementException import HOTELMANAGEMENTEXCEPTION

from .HotelReservation import HOTELRESERVATION


class HOTELMANAGER:
    """Class HotelManager"""
    def __init__(self):
        pass

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
    def VALIDATE_PHONE_NUMBER(self, strPhoneNumber:str) -> bool:
        if len(strPhoneNumber) != 9:
            return False
        intList = [int(intNum) for intNum in strPhoneNumber[:-1]]
        for i in intList:
            if i != (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
                return False
        return True

    def VALIDATE_DAYS(self, intDays) -> bool:
        if type(intDays) == str:
            return False
        if 0 < intDays < 11:
            return True
        return False


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
    @staticmethod
    def valida_id(id):
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

    @staticmethod
    def valida_room(strRoom):
        """Devuelve True si el tipo de habitación es válido, sino False"""
        if not isinstance(strRoom, str):
            return False
        if strRoom.lower not in ("single", "double", "suite"):
            return False
        return True

    def room_reservation(self, strIdCard, strCreditCardNum, strNameAndSurname, strPhoneNumber, strRoomType, intNumDays)
        if not self.valida_id(strIdCard):
            raise HotelManagerException("ID no valido")
        if not self.valida_room(strRoomType):
            raise HotelManagerException("Tipo de habitación no válido")