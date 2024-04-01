''' Class HotelManager (GE2.2) '''
import re
import json
from pathlib import Path
from datetime import datetime
import time
from .HotelStay import HOTELSTAY
from .HotelManagementException import HotelManagementException
from .HotelReservation import HOTELRESERVATION

class HotelManager:
    """Class HotelManager"""
    def __init__(self):
        pass

    @staticmethod
    def VALIDATENAMEANDSURNAME(strNameAndSurname) -> bool:
        if type(strNameAndSurname) != str:
            return False

        if (len(strNameAndSurname) <= 10) or (len(strNameAndSurname) >= 50):
            return False

        for char in strNameAndSurname:
            if char in '1234567890':
                return False

        if ' ' not in strNameAndSurname:
            return False
        return True

    @staticmethod
    def VALIDATECREDITCARD(strCreditCardNum: str) ->bool:
        if type(strCreditCardNum) != str:
            return False
        #Comprobar la longitud de la tarjeta de credito
        if len(strCreditCardNum) != 16:
            return False
        try:
            int(strCreditCardNum)
        except ValueError:
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

    @staticmethod
    def VALIDATE_PHONE_NUMBER(strPhoneNumber:str) -> bool:
        if type(strPhoneNumber) != str:
            return False
        if len(strPhoneNumber) != 9:
            return False
        try:
            int(strPhoneNumber)
        except ValueError:
            return False
        intList = [int(intNum) for intNum in strPhoneNumber]
        for i in intList:
            if i not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 0):
                return False
        return True

    @staticmethod
    def VALIDATE_DAYS(intDays) -> bool:
        if type(intDays) != int:
            return False
        if 0 < intDays < 11:
            return True
        return False

    @staticmethod
    def VALIDATE_ID(id):
        """Devuelve True si el id entregado es válido, sino False"""
        if type(id) != str:
            return False
        intId = id[:-1]
        if not isinstance(id, str) or len(id) != 9:
            return False
        try:
            int(intId)
        except ValueError:
            return False
        strLetras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        intIndex = int(intId) % 23
        return id[-1].upper() == strLetras[intIndex]

    @staticmethod
    def VALIDATE_ROOM_TYPE(strRoom):
        """Devuelve True si el tipo de habitación es válido, sino False"""
        if not isinstance(strRoom, str):
            return False
        if strRoom.lower() not in ("single", "double", "suite"):
            return False
        return True


    def REGISTER_RESERVATION(self, strCreditCard, strIdCard, strNameSurname, strPhoneNumber, strRoomType, intNumDays):
        if not self.VALIDATECREDITCARD(strCreditCard):
            raise HotelManagementException("Creditcard not valid")
        if not self.VALIDATE_ID(strIdCard):
            raise HotelManagementException("ID not valid")
        if not self.VALIDATENAMEANDSURNAME(strNameSurname):
            raise HotelManagementException("Name not valid")
        if not self.VALIDATE_PHONE_NUMBER(strPhoneNumber):
            raise HotelManagementException("Phone number not valid")
        if not self.VALIDATE_ROOM_TYPE(strRoomType):
            raise HotelManagementException("Room type not valid")
        if not self.VALIDATE_DAYS(intNumDays):
            raise HotelManagementException("Number of days not valid")ç


        #Creamos la ruta que lleva hasta el proyecto
        strArchivoAlmacenaje = str(Path.home())
        strArchivoAlmacenaje += "/PycharmProjects/G842024.T10.EG2/src/JSONfiles/HotelReserves.json"

        #Creamos un objeto del tipo reserva
        my_reservation = HOTELRESERVATION(strIdCard, strCreditCard, strNameSurname, strPhoneNumber, strRoomType,
                                         intNumDays)

        """EMPEZAMOS A ABRIR EL FICHERO JSON. PRIMERO LEEMOS EL ARCHIVO Y LUEGO ESCRIBIMOS EN EL"""

        #COMENZAMOS A LEER EL ARCHIVO
        try:
            #Abrimos el fichero json y añadimos toda la información a una lista.
            with open(strArchivoAlmacenaje, "r", encoding="utf-8", newline="") as file:
                lstListaDatos = json.load(file)
        except FileNotFoundError:
            # El archivo no se ha encontrado
            lstListaDatos = []
        except json.JSONDecodeError as ex:
            #Ocurre un error al decodificar el archivo
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #Añadimos la reserva que hemos hecho a la lista de datos.
        lstListaDatos.append(my_reservation.__str__())

        #COMENZAMOS A ESCRIBIR EN EL ARCHIVO
        try:
            #Abrimos otra vez el fichero y comenzamos a meter toda la información en él.
            with open(strArchivoAlmacenaje, "w", encoding="utf-8", newline="") as file:
                json.dump(lstListaDatos, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file or file path") from ex

        return my_reservation.LOCALIZER


    def READDATAFROMJSON(self, strFi):
        try:
            with open(strFi) as f:
                strData = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e
        try:
            strC = strData["CreditCard"]
            strP = strData["phoneNumber"]
            req = HOTELRESERVATION(strIdCard="12345678Z", strCreditCardNum=strC, strNameAndSurname="John Doe",
                                    strPhoneNumber=strP, strRoomType="single", intNumDays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.VALIDATECREDITCARD(strC): raise HotelManagementException("Invalid credit card number")
        #Cerramos el archivo
        return req

    """A CONTINUACION CREAMOS FUNCIONES PARA VALIDAR LAS ENTRADAS DEL MÉTODO 2
    ESTAS ENTRADAS SON EL LOCALIZADOR, (HASH) Y EL DNI DEL CLIENTE. LA FUNCION DE VALIDAR DNI ESTA ARRIBA. """

    @staticmethod
    def VALIDATELOCALIZER(strLocalizer) -> bool:
        """Validamos el valor del md5"""
        #En primer lugar, comprobamos el tipo del localizador
        if type(strLocalizer) != str:
            return False
        #A continuación, comprobamos la longitud del localizador.
        if len(strLocalizer) != 32:
            return False
        #Como un está en hexadecimal, comprobamos:
        for i in strLocalizer:
            if i not in "abcdef0123456789":
                return False
        return True


    """COMENZAMOS EL METODO 2: LLEGADA AL HOTEL"""
    def GUESTARRIVAL(self, ruta_archivo):
        #Obtenemos toda la informacion del archivo de entrada
        try:
            #Leemos el archivo
            with open(ruta_archivo, "r", encoding="utf-8", newline="") as file:
                input_data = json.load(file)
        except FileNotFoundError as ex:
            #Lanzamos excepcion si no se encuentra el archivo
            raise HotelManagementException("Input file not found.") from ex
        except json.JSONDecodeError as ex:
            # Ocurre un error al decodificar el archivo
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format.") from ex
        try:
            strLocalizer = input_data["Localizer"]
            strID = input_data["ClientID"]
        except KeyError as ex:
            raise HotelManagementException("Invalid Keys in input File.") from ex
        if not self.VALIDATELOCALIZER(strLocalizer):
            raise HotelManagementException("The Localizer is not valid." )
        if not self.VALIDATE_ID(strID):
            raise HotelManagementException("The ID is not valid.")

        """A CONTINUACION CARGAMOS EL FICHERO CON LA INFORMACION DE LA RESERVA"""
        strArchivoAlmacenaje = self.RUTAARCHIVOJSON()
        strArchivoAlmacenaje += "HotelReserves.json"


        """Cargamos los datos del fichero json a una lista"""
        try:
            #Volvemos a leer el fichero otra vez
            with open(strArchivoAlmacenaje, "r", encoding="utf-8", newline="") as file:
                lstListaDatos = json.load(file)
        except FileNotFoundError as ex:
            #Lanzamos una excepcion si no se encuentra el archivo JSON
            raise HotelManagementException("JSON File Not Found.") from ex
        except json.JSONDecodeError as ex:
            #Lanzamos una excepcion al decodificar el archivo json
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format.") from ex


            """CAMBIAR A PARTIR DE AQUI"""

            # Buscamos ela reserva y preparamos los datos para ser guardados.
            boolEncontrado = False
            for hotel_reservation in lstListaDatos:
                if hotel_reservation["HotelReservation__Localizer"] == strLocalizer:
                    strLocalizer = hotel_reservation["HotelReservation__strLocalizer"]
                    strIdCard = hotel_reservation["HotelReservation__strIdCard"]
                    boolEncontrado = True
                    break
            if not boolEncontrado:
                raise HotelManagementException("The hotel reservation has not been found.")

            """AHORA CREAMOS UNA LLEGADA AL HOTEL"""
            my_hotel_stay = HOTELSTAY(strLocalizer, strIdCard, intNumDays, strRoomType)


            #A continuación creamos la ruta al archivo de almacenaje
            strArchivoAlmacenaje = self.RUTAARCHIVOJSON()
            strArchivoAlmacenaje += "HotelStays.json"

            try:
                #VOLVEMOS A LEER EL FICHERO Y CARGAMOS LOS CONTENIDOS EN LISTA DE DATOS
                with open(strArchivoAlmacenaje, "r", encoding="utf-8", newline="") as file:
                    lstListaDatos = json.load(file)
            except FileNotFoundError:
                #El fichero no ha sido encontrado
                lstListaDatos = []
            except json.JSONDecodeError as ex:
                #Creamos una excepcion si no se puede decodificar el archivo
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

            lstListaDatos.append(my_hotel_stay.__dict__)

            try:
                # Ahora abrimos el fichero JSON para escribir toda la infromación en el
                with open(strArchivoAlmacenaje, "w", encoding="utf-8", newline="") as file:
                    json.dump(lstListaDatos, file, indent=2)
            except FileNotFoundError as ex:
                #Lanzamos una Excepcion si no se ha encontrado
                raise HotelManagementException("Invalid file or path to file") from ex

            #DEVOLVEMOS LA LLAVE DE LA HABITACION DEL HOTEL
            return my_hotel_stay.strRoomKey

    @staticmethod
    def VALIDATESHAH256(strRoomKey):
    #Validamos que el strRoomKey cumple con el formato del shah-256
        if type(strRoomKey) != str or len(strRoomKey)!= 64:
            #Comrpobamos la longitud y el tipo
            return False
        for i in strRoomKey:
            #Comprobamos que esta escrito en hexadecimal y es valido
            if i not in "abcdef1234567890":
                return False
        return True

    """COMENZAMOS LA TERCERA FUNCION: CHECKOUT"""

    def CHECKOUT(self, strRoomKey):
        #EN PRIMER LUGAR, COMPROBAMOS LA VALIDEZ DE LA LLAVE DE HABITACION
        if not self.VALIDATESHAH256(strRoomKey):
            raise HotelManagementException("Error: invalid room key.")

