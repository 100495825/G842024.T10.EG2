import os
import json
import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException


class MyTestCase(unittest.TestCase):
    """CLASE QUE COMPRUEBA EL MÉTODO 3: FUNCION CHECKOUT"""
    def test_ruta_1(self):
        #test para el camino: 1-2-4-7-8-9-10-12-15
        my_manager = HotelManager()
        with freeze_time("2024-03-18"):
            my_manager.REGISTER_RESERVATION(
                strCreditCard="5105105105105100",
                strIdCard="15459426E",
                strNameSurname="Marta Rodriguez",
                strPhoneNumber="689677660",
                strRoomType="single",
                intNumDays=6,)
        my_hotel_stay = my_manager.GUESTARRIVAL(self.ruta_json + "TESTRUTA1.json")
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("6ebb8a1c790b34921640zy5539786250")
        self.assertEqual("The hotel room key has not been found.", ome.exception.message)
        with freeze_time("2024-03-20"):
            my_manager.CHECKOUT(my_hotel_stay)

        with open(self.HotelCheckout, "r", encoding="utf-8", newline="") as file:
            datos = json.load(file)

        for hora in datos:
            if hora['strRoomKey'] == my_hotel_stay:
                intValorHora = my_hotel_stay
            else:
                intValorHora = 0

        self.assertEqual(intValorHora, "21cc45d1770dd1b5257e7377f08ced110b1ae54bd137fba63e46632d0831c402")
    def test_ruta_2(self):
        #test para el camino: 1-2-4-7-8-9-11-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("12wq0293fd7181623dc69e4d9674a"
                                       "esed367123985jkdc5dplofe7726816df91")
        self.assertEqual("The hotel room key has not been found.", ome.exception.message)


    def test_ruta_3(self):
        #test para el camino: 1-2-4-7-8-9-10-13-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("12wq0293fd7181623dc69e4d9674a"
                                       "esed367123985jkdc5dplofe7726816df91")
        self.assertEqual("Invalid file or path to file", ome.exception.message)



    def test_ruta_4(self):
        #test para el camino: 1-2-5-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("12wq0293fd7181623dc69e4d9674a"
                                       "esed367123985jkdc5dplofe7726816df91")

        self.assertEqual("Error: File not found", ome.exception.message)

    def test_ruta_5(self):
        #test para el camino: 1-2-6-14
        my_manager = HotelManager()
        with open(self.HotelStays, "w", encoding="utf-8", newline="") as file:
            file.write("Wrong json format")
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("029f0293fd7181623dc69e4d9674a"
                                       "beed367a3c985c31c5dbedfe7726816df91")

        self.assertEqual("JSON Decode Error - Wrong JSON Format", ome.exception.message)

    def test_ruta_6(self):
        #test para el camino: 1-3-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("029f0293fd7181623dc69e4d9674a")

        self.assertEqual("Error: invalid room key.", ome.exception.message)


    if __name__ == '__main__':
        unittest.main()
