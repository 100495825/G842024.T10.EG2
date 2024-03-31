"""Clase para comprobar una Reserva de Hotel"""
import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException


class MyTestCase(unittest.TestCase):
    """TESTS RELACIONADOS CON EL NUMERO DE LA TARJETA DE CRÉDITO"""

    @freeze_time("2024-03-18")
    def test_ec_v1(self):
        """ Test ec v1: El Numero de la tarjeta de credito es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(


        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv1(self):
        """ Test ec nv 1: El numero de la tarjeta de credito contiene letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("La tarjeta de crédito no es válida", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv2(self):
        """ Test ec nv 2: La tarjeta de crédito contiene más de 17 dígitos"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de tarjeta tiene demasiados dígitos", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv3(self):
        """ Test ec nv 3: La tarjeta de crédito tiene menos de 15 dígitos"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número no contiene suficientes dígitos", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv4(self):
        """ Test ec nv 4: El número no cumple el algoritmo de Luhn"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El numero de la tarjeta no es válido.", ome.exception.message)

    @freeze_time("2023-03-08")
    def test_ec_nv5(self):
        """ Test ec nv 5: El número no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El numero de la tarjeta no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL DNI DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_v2(self):
        """ Test ec v2: El DNI es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv6(self):
        """ Test ec nv 6: EL DNI contiene demasiadas letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv7(self):
        """ Test ec nv 7: EL DNI contiene letras inválidas"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv8(self):
        """ Test ec nv 8: EL DNI contiene demasiados caracteres"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv9(self):
        """ Test ec nv 9: EL DNI no contiene suficientes caracteres"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv10(self):
        """ Test ec nv 10: EL DNI no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("EL DNI no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NOMBRE Y APELLIDO DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_v3(self):
        """ Test ec v1: El nombre del cliente es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv11(self):
        """ Test ec nv 11: El nombre del cliente contiene números"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv12(self):
        """ Test ec nv 12: El nombre del cliente no tiene espacios"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv13(self):
        """ Test ec nv 13: El nombre del cliente no tiene espacios"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv14(self):
        """ Test ec nv 14: El nombre del cliente es demasiado corto"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv15(self):
        """ Test ec nv 15: El nombre del cliente es demasiado largo"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv16(self):
        """ Test ec nv 16: El nombre del cliente no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El nombre no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NUMERO DE TELEFONO DEL CLIENTE"""

    @freeze_time("2024-03-18")
    def test_ec_v4(self):
        """ Test ec v4: El número del cliente es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv17(self):
        """ Test ec nv 17: El número del cliente es demasiado corto"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv18(self):
        """ Test ec nv 18: El número del cliente es demasiado largo"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv19(self):
        """ Test ec nv 19: El número del cliente contiene letras"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv20(self):
        """ Test ec nv 20: El número del cliente no se guarda como string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de teléfono no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON EL TIPO DE HABITACION"""

    @freeze_time("2024-03-18")
    def test_ec_v5(self):
        """ Test ec v5: El tipo de habitación es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_v6(self):
        """ Test ec v6: El tipo de habitación es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_v7(self):
        """ Test ec v7: El tipo de habitación es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv21(self):
        """ Test ec nv 21: El tipo de habitación no existe"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El tipo de habitación no es válido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv22(self):
        """ Test ec nv 22: El tipo de habitación no es un string"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El tipo de habitación no es válido.", ome.exception.message)

    """TESTS RELACIONADOS CON LA FECHA DE LLEGADA"""

    @freeze_time("2024-03-18")
    def test_ec_v8(self):
        """ Test ec v8: La fecha de llegada es válida"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv23(self):
        """ Test ec nv 23: La fecha de llegada no es un date"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("La fecha de llegada es inválida.", ome.exception.message)

    """TESTS RELACIONADOS CON EL NÚMERO DE DÍAS"""

    @freeze_time("2024-03-18")
    def test_ec_v9(self):
        """ Test ec v9: El número de días es válido"""
        my_manager = HotelManager()
        my_reservation_localizer = my_manager.REGISTER_RESERVATION(

        )
        self.assertEqual(my_reservation_localizer, '#')

    @freeze_time("2024-03-18")
    def test_ec_nv24(self):
        """ Test ec nv 24: El número de días es demasiado grande"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv25(self):
        """ Test ec nv 25: El número de días es menor que 1"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_ec_nv26(self):
        """Test ec nv 26: El número de días no es un número"""
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.REGISTER_RESERVATION(

            )
        self.assertEqual("El número de días es inválido.", ome.exception.message)







