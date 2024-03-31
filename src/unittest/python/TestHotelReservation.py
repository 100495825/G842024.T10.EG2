import unittest
import datetime
from UC3MTravel import HOTELMANAGEMENTEXCEPTION
from UC3MTravel import HOTELMANAGER
from freezegun import freeze_time
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
class TESTS_RESERVE(unittest.TestCase):
    @freeze_time("2024-03-31")
    def TESTDAYS_C1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A" ,
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays= 5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')

    def TESTDAYS_CN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123475869",
                                                           strRoomType="Single",
                                                           intNumDays=5.6)
        self.assertEqual("Number of days not valid", HME.exception.MESSAGE)
    def TESTDAYS_CN2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123475869",
                                                           strRoomType="Single",
                                                           intNumDays=555)
        self.assertEqual("Number of days not valid", HME.exception.MESSAGE)
    def TESTDAYS_CN3(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123475869",
                                                           strRoomType="Single",
                                                           intNumDays="a")
        self.assertEqual("Number of days not valid", HME.exception.MESSAGE)
    def TESTDAYS_VL1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A" ,
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays= 10)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')
    def TESTDAYS_VL2(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A" ,
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays= 9)

        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')
    def TESTDAYS_VL3(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A" ,
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays= 1)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')
    def TESTDAYS_VL4(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A" ,
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays= 2)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')
    def TESTDAYS_VLN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123475869",
                                                           strRoomType="Single",
                                                           intNumDays=11)
        self.assertEqual("Number of days not valid", HME.exception.MESSAGE)
    def TESTDAYS_VLN2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123475869",
                                                           strRoomType="Single",
                                                           intNumDays=0)
        self.assertEqual("Number of days not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_C1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                       strId_Card="12345124P",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays=5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')
    def TESTSPHONENUMBER_CN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="12347589999969",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_CN2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_CN3(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="123apo345",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_CN4(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="apppppppp",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_VNL1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="1234567890",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)
    def TESTSPHONENUMBER_VNL2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                           strId_Card="12345124P",
                                                           strNameSurname="Juanjo Sanchez",
                                                           strPhoneNumber="12345678",
                                                           strRoomType="Single",
                                                           intNumDays=5)
        self.assertEqual("Phone number not valid", HME.exception.MESSAGE)

    def TEST_ID_C1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                       strId_Card="12345124Y",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays=5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')

    def TEST_ID_CN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="12345124P",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_CN2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="123451249",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_CN3(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="1234a124Y",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_CN4(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="12345124",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_CN5(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="123451249Y",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_CN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="12345124P",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_VL1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                       strId_Card="12345124Y",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays=5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')

    def TEST_ID_VLN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="12345124YY",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ID_VLN2(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="1234512Y",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType="Single",
                                            intNumDays=5)
        self.assertEqual("ID not valid", HME.exception.MESSAGE)

    def TEST_ROOM_TYPE_C1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                       strId_Card="12345124Y",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="suite",
                                                       intNumDays=5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')

    def TEST_ROOM_TYPE_CN1(self):
        my_manager = HOTELMANAGER()
        with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
            my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                            strId_Card="12345124Y",
                                            strNameSurname="Juanjo Sanchez",
                                            strPhoneNumber="123475869",
                                            strRoomType=4,
                                            intNumDays=5)
        self.assertEqual("Room type not valid", HME.exception.MESSAGE)

    def TEST_ROOM_TYPE_VL1(self):
        my_manager = HOTELMANAGER()
        my_reserveID = my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                       strId_Card="12345124Y",
                                                       strNameSurname="Juanjo Sanchez",
                                                       strPhoneNumber="123475869",
                                                       strRoomType="Single",
                                                       intNumDays=5)
        self.assertEqual(my_reserveID, '348515e8e2ec22aebe7e3f831e8b7807')

        def TEST_ROOM_TYPE_VLN1(self):
            my_manager = HOTELMANAGER()
            with self.assertRaises(HOTELMANAGEMENTEXCEPTION) as HME:
                my_manager.REGISTER_RESERVATION(strCreditCard="510051005100510A",
                                                strId_Card="12345124P",
                                                strNameSurname="Juanjo Sanchez",
                                                strPhoneNumber="123475869",
                                                strRoomType="doble",
                                                intNumDays=11)
            self.assertEqual("Room type not valid", HME.exception.MESSAGE)


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
class TEST_VALID_ROOM_TYPE(unittest.TestCase):
    def TEST_VALID_ROOM_TYPE(self):
        #Comprobamos una habitación válida
        strRoomType= "suite"
        self.assertTrue(VALIDATE_ROOM_TYPE(strRoomType))
    def TEST_INVALID_ROOM_TYPE(self):
         #Comrpobamos una habitación cuyo nombre no es correcto
         strRoomType = "doble"
         self.assertFalse(VALIDATE_ROOM_TYPE(strRoomType))
class TEST_VALID_ID(unittest.TestCase):
    def TEST_VALID_ID(self):
        #Comprobamos un ID válido
        strIdCard="12345124Y"
        self.assertTrue(VALIDATE_ID(strIdCard))
    def TEST_INVALID_LENGHT(self):
        #Comprobamos un ID con una longitud no permitida
        strIdCard="1234567P"
        self.assertFalse(VALIDATE_ID(strIdCard))
    def TEST_INVALID_DIGIT(self):
        #Comrpobamos un ID con dígitos no válidos
        strIdCard="12345a24Y"
        self.assertFalse(VALIDATE_ID(strIdCard))
    def TEST_NO_LETTER(self):
        #Comprobamos un ID sin letra
        strIdCard="12345124"
        self.assertFalse(VALIDATE_ID(strIdCard))