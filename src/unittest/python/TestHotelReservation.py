import unittest
import datetime
import re


def  VALIDATECREDITCARD(strCreditCardNum) ->bool:
    #Comprobar la longitud de la tarjeta de credito
    if len(strCreditCardNum) != 16:
        return False
    intChecksum = int(strCreditCardNum[-1])
    #Metemos los numeros en una lista
    lstNumeros = [int(intNum) for intNum in strCreditCardNum[:-1]]

    # Duplicamos los numeros en las posiciones pares empezando por 1
    lstNumeros = [lstNumeros[i] * 2 if i % 2 == 0 else lstNumeros[i] for i in range(len(lstNumeros))]

    # Sumamos los digitos de los numeros mayores a 9
    lstNumeros = [sum([int(num) for num in str(lstNumeros[i])]) if lstNumeros[i] > 9 else lstNumeros[i] for i in range(len(lstNumeros))]

    # Sumamos todos los numeros y calculamos el checksum teorico
    intSuma = sum(lstNumeros)
    intChecksumTeorica = intSuma * 9 % 10

    return intChecksum == intChecksumTeorica



def VALIDATENAMESURNAME(strNameAndSurname)->bool:
    if (len(strNameAndSurname) <= 10) or (len(strNameAndSurname) >= 50):
        return False

    for char in strNameAndSurname:
        if char in '1234567890':
            return False

    if ' ' not in strNameAndSurname:
        return False


def VALIDATEDATEFORMAT(dateArrival)-> bool:
    strValidFormat = re.match(r'\d{2}/\d{2}/\d{4}', dateArrival)
    return strValidFormat is not None

class TEST_VALID_CREDIT_CARD(unittest.TestCase):
    def TEST_VALID_CARD(self):
        strCard = "4188202133102069"
        self.assertTrue(VALIDATECREDITCARD(strCard))

    def TEST_INVALID_CARD(self):
        strCard = "23458172934"
        self.assertFalse(VALIDATECREDITCARD(strCard))

    def TEST_INVALID_LENGTH_BELOW(self):
        #Establecemos valor limite por debajo (15)
        strCard = "123456789123434"
        self.assertFalse(VALIDATECREDITCARD(strCard))

    def TEST_INVALID_LENGTH_ABOVE(self):
        #Establecemos el valor limite por encima (17)
        strCard = "12345678912345678"
        self.assertFalse(VALIDATECREDITCARD(strCard))
    def TEST_BELOW_LOWEST_LENGTH(self):
        #ESTABLECEMOS CLASE DE EQUIVALENCIA CON CUALQUIER VALOR POR DEBAJO DEL MINIMO
        strCard = "48832021331029"
        self.assertFalse(VALIDATECREDITCARD(strCard))
    def TEST_ABOVE_GREATEST_LENGTH(self):
        # ESTABLECEMOS CLASE DE EQUIVALENCIA CON CUALQUIER VALOR POR ENCIMA DEL MAXIMO
        strCard ="418282021331020691"
        self.assertFalse(VALIDATECREDITCARD(strCard))

class TEST_VALID_NAME_AND_SURNAME(unittest.TestCase):
    def TEST_VALID_NAME(self):
        #Comprobamos un Nombre valido
        strNameAndSurname = "Marta Rodriguez"
        self.assertTrue(VALIDATENAMESURNAME(strNameAndSurname))

    def TEST_MAX_NAME_LENGTH(self):
        #Comprobamos un nombre valido que esta en el limite superior
        strNameAndSurname = "Paula Beatriz Diez de Baldeon Sanchez de Mendoza"
        self.assertTrue(VALIDATENAMESURNAME(strNameAndSurname))

    def TEST_MIN_NAME_LENGTH(self):
        #Comprobamos un nombre valido que esta en el limite inferior
        strNameAndSurname = "Ana Gonzalez"
        self.assertTrue(VALIDATENAMESURNAME(strNameAndSurname))
    def TEST_NUMBERS_IN_NAME(self):
        #Comprobamos si hay numeros en el nombre
        strNameAndSurname = "Pablo9 Rodriguez"
        self.assertFalse(VALIDATENAMESURNAME(strNameAndSurname))
    def TEST_NO_SPACE_IN_NAME(self):
        #Comprobamos si no hay espacio en el nombre
        strNameAndSurname = "FernandoRomero"
        self.assertFalse(VALIDATENAMESURNAME(strNameAndSurname))

    def TEST_BELOW_MIN_LENGTH_IN_NAME(self):
        #Eliminamos nombres que no cumplan el minimo
        strNameAndSurname = "Noa Lopez"
        self.assertFalse(VALIDATENAMESURNAME(strNameAndSurname))

    def TEST_ABOVE_MAX_LENGTH(self):
        #Eliminamos nombres que esten por encima del maximo
        strNameAndSurname = "Marta Beatriz Diez de Baldeon Sanchez del Pinar y Ortiz"
        self.assertFalse(VALIDATENAMESURNAME(strNameAndSurname))

class TEST_VALID_ARRIVAL_DATE(unittest.TestCase):
    def TEST_ARRIVAL_DATE_FORMAT(self):
        #Comprobamos que cumple el formato adecuado
        dateArrival = datetime.utcnow()
        self.assertTrue(VALIDATEDATEFORMAT(dateArrival))