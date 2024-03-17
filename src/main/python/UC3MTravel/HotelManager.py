''' Class HotelManager (GE2.2) '''

import json

from .HotelManagementException import HOTELMANAGMENTEXCEPTION

from .HotelReservation import HOTELRESERVATION


class HOTELMANAGER:
    def __init__( self ):
        pass

    def VALIDATECREDITCARD(self, strCreditCardNum:str ) ->bool:
            #Comprobar la longitud de la tarjeta de credito
            if (len(strCreditCardNum) != 16):
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

    def READDATAFROMJSON( self, strFi ):

        try:
            with open( strFi ) as f:
                strData = json.load( f )
        except FileNotFoundError as e:
            raise HOTELMANAGMENTEXCEPTION("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HOTELMANAGMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from e

        try:
            strC = strData[ "CreditCard" ]
            strP = strData[ "phoneNumber" ]
            req = HOTELRESERVATION( IDCARD="12345678Z", creditcardNumb=strC, nAMeAndSURNAME="John Doe",
                                    phonenumber=strP, room_type="single", numdays=3 )
        except KeyError as e:
            raise HOTELMANAGMENTEXCEPTION("JSON Decode Error - Invalid JSON Key") from e
        if not self.VALIDATECREDITCARD(strC): raise HOTELMANAGMENTEXCEPTION("Invalid credit card number")

        # Close the file
        return req
