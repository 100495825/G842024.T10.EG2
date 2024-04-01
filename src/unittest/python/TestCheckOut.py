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

    if __name__ == '__main__':
        unittest.main()
