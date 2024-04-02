import os
import json
import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException

class MyTestCase(unittest.TestCase):
    """CLASE QUE COMPRUEBA EL MÉTODO 3: FUNCION CHECKOUT"""

    def setUp(self):
        #ESTABLECEMOS LA RUTA DE CADA COMPONENTE A SU RESPECTIVO FICHERO JSON
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        self.HotelStays = self.ruta_json+ "HotelStays.json"
        self.HotelCheckout = self.ruta_json + "HotelCheckout.json"
        self.HotelReserves = self.ruta_json + "HotelReserves.json"

        #ABRIMOS CADA UNO DE LOS ARCHIVOS PARA LEER LOS CONTENIDOS
        try:
            with open(self.HotelReserves, "r", encoding="utf-8", newline="") as file:
                self.reservesData = json.load(file)
        except FileNotFoundError as exc:
            raise Exception("File not found.") from exc

        try:
            with open(self.HotelStays, "r", encoding="utf-8", newline="") as file:
                self.staysData = json.load(file)
        except FileNotFoundError as exc:
            raise Exception("File not found.") from exc

        try:
            with open(self.HotelCheckout, "r", encoding="utf-8", newline="") as file:
                self.checkoutData = json.load(file)
        except FileNotFoundError:
            self.data_time = []

        os.remove(self.HotelReserves)
        os.remove(self.HotelStays)
        os.remove(self.HotelCheckout)

    def tearDown(self):
        #ABRIMOS OTRA VEZ LOS FICHEROS ANTES DE CERRAR PARA ESCRIBIR EN ELLOS
        try:
            with open(self.HotelReserves, "w", encoding="utf-8", newline="") as file:
                json.dump(self.reservesData, file, indent=2)
        except FileNotFoundError as ex:
            raise Exception("File not found.") from ex

        try:
            with open(self.HotelStays, "w", encoding="utf-8", newline="") as file:
                json.dump(self.staysData, file, indent=2)
        except FileNotFoundError as ex:
            raise Exception("File not found.") from ex

        try:
            with open(self.HotelCheckout, "w", encoding="utf-8", newline="") as file:
                json.dump(self.checkoutData, file, indent=2)
        except FileNotFoundError as ex:
            raise Exception("File not found.") from ex

    def test_st_path_4(self):
        #test para el camino: 1-2-5-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("12wq0293fd7181623dc69e4d9674a"
                                       "esed367123985jkdc5dplofe7726816df91")

        self.assertEqual("Error: File not found", ome.exception.message)

    def test_st_path_5(self):
        #test para el camino: 1-2-6-14
        my_manager = HotelManager()
        with open(self.HotelStays, "w", encoding="utf-8", newline="") as file:
            file.write("Wrong json format")
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("029f0293fd7181623dc69e4d9674a"
                                       "beed367a3c985c31c5dbedfe7726816df91")

        self.assertEqual("JSON Decode Error - Wrong JSON Format", ome.exception.message)

    def test_st_path_6(self):
        #test para el camino: 1-3-14
        my_manager = HotelManager()
        with self.assertRaises(HotelManagementException) as ome:
            my_manager.CHECKOUT("029f0293fd7181623dc69e4d9674a")

        self.assertEqual("Error: invalid room key.", ome.exception.message)
    if __name__ == '__main__':
        unittest.main()
