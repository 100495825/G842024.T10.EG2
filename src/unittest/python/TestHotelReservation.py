"""Clase para comprobar una Reserva de Hotel"""

import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException


class MyTestCase(unittest.TestCase):
    """TESTS RELACIONADOS CON EL NUMERO DE LA TARJETA DE CRÉDITO"""

    @freeze_time("2024-03-18")
    def test_ec_v1(self):
        """ Test ec v1: Valores Válidos"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(
            strCreditCard="5105105105105100",
            strIdCard="15459426E",
            strNameSurname="Marta Rodriguez",
            strPhoneNumber="689677660",
            strRoomType="single",
            intNumDays=6,
        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv1(self):
        """ Test ec nv 1: El numero de la tarjeta de credito contiene letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="510510510510510A",
                strIdCard="12345678Z",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("La tarjeta de crédito no es válida", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv2(self):
        """ Test ec nv 2: La tarjeta de crédito contiene más de 17 dígitos"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="51051051051051001",
                strIdCard="12345678Z",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número de tarjeta tiene demasiados dígitos", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv3(self):
        """ Test ec nv 3: La tarjeta de crédito tiene menos de 15 dígitos"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="510510510510510",
                strIdCard="12345678Z",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número no contiene suficientes dígitos", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv4(self):
        """ Test ec nv 4: El número no cumple el algoritmo de Luhn"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="1234567890123456",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El numero de la tarjeta no es válido.", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv5(self):
        """ Test ec nv 5: El número no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard=5105105105105100,
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El numero de la tarjeta no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL DNI DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_nv6(self):
        """ Test ec nv 6: EL DNI contiene demasiadas letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="1234Y5124",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv7(self):
        """ Test ec nv 7: EL DNI contiene letras inválidas"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124P",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv8(self):
        """ Test ec nv 8: EL DNI contiene demasiados caracteres"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="123451245Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv9(self):
        """ Test ec nv 9: EL DNI no contiene suficientes caracteres"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="1234512Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv10(self):
        """ Test ec nv 10: EL DNI no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard=12345124,
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NOMBRE Y APELLIDO DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_nv11(self):
        """ Test ec nv 11: El nombre del cliente contiene números"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta9 Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv12(self):
        """ Test ec nv 12: El nombre del cliente no tiene espacios"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="MartaRodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv13(self):
        """ Test ec nv 13: El nombre del cliente es demasiado corto"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Ana Gil",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv14(self):
        """ Test ec nv 14: El nombre del cliente es demasiado largo"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Maria Beatriz Diez de Baldeon Sanchez del Pinar y Ortiz",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv15(self):
        """ Test ec nv 15: El nombre del cliente no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname=1234567,
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NUMERO DE TELEFONO DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_nv16(self):
        """ Test ec nv 16: El número del cliente es demasiado corto"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv17(self):
        """ Test ec nv 17: El número del cliente es demasiado largo"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="6896776606",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv18(self):
        """ Test ec nv 18: El número del cliente contiene letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="68967766a",
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv19(self):
        """ Test ec nv 19: El número del cliente no se guarda como string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber=689677660,
                strRoomType="single",
                intNumDays=6,
            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL TIPO DE HABITACION"""

    @freeze_time("2024-03-18")
    def test_ec_v2(self):
        """ Test ec v2: El tipo de habitación es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(
            strCreditCard="5105105105105100",
            strIdCard="12345124Y",
            strNameSurname="Marta Rodriguez",
            strPhoneNumber="689677",
            strRoomType="double",
            intNumDays=6,
        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_v3(self):
        """ Test ec v3: El tipo de habitación es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(
            strCreditCard="5105105105105100",
            strIdCard="12345124Y",
            strNameSurname="Marta Rodriguez",
            strPhoneNumber="689677",
            strRoomType="suite",
            intNumDays=6,
        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv20(self):
        """ Test ec nv 20: El tipo de habitación no existe"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="triple",
                intNumDays=6,
            )
        self.assertEqual("El tipo de habitación no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv21(self):
        """ Test ec nv 21: El tipo de habitación no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType=1234,
                intNumDays=6,
            )
        self.assertEqual("El tipo de habitación no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NÚMERO DE DÍAS"""

    @freeze_time("2024-03-18")
    def test_ec_nv22(self):
        """ Test ec nv 22: El número de días es demasiado grande"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="single",
                intNumDays=11,
            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv23(self):
        """ Test ec nv 23: El número de días es menor que 1"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="single",
                intNumDays=-1,
            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv24(self):
        """Test ec nv 24: El número de días no es un número"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="single",
                intNumDays="abc",
            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv24(self):
        """Test ec nv 24: El número de días es un float"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="12345124Y",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677",
                strRoomType="single",
                intNumDays=2.4,
            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)







