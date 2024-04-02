"""CLASE PARA COMPROBAR UNA LLEGADA AL HOTEL"""
import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException

class MyTestCase(unittest.TestCase):
    """TESTS DE LA FUNCION DE LLEGADA AL HOTEL"""
    @freeze_time("2024-03-18")
    def test_v1(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        mi_roomKey = mi_manager.GUESTARRIVAL("/Users/mariaromeromartin/PycharmProjects/G842024.T10.EG2/src/JSONfiles/TestsSegundaFuncion/TEST1.json")
        self.assertEqual(mi_roomKey, "6ebb8a1c790b3492164055397862500c")


    @freeze_time("2024-03-18")
    def test_nv1(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST2.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv2(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST3.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv3(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST4.json")
        self.assertEqual("Input not found in file.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv4(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST5.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv5(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST6.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv6(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST7.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv7(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST8.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv8(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST9.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv9(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST10.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv10(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST11.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv11(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST12.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv12(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST13.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv13(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST14.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv14(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST13.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv15(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST14.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv16(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST15.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv17(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST16.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv18(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST17.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv19(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST18.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv20(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST19.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv21(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST20.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv22(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST21.json")
        self.assertEqual("Input not found in file.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv23(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST22.json")
        self.assertEqual("Input not found in file.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv24(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST23.json")
        self.assertEqual("JSON Decode Error - Wrong JSON Format.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv25(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST24.json")
        self.assertEqual("Input not found in file.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv26(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST25.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv27(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST26.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv28(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST27.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv29(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST28.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv30(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST29.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv31(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST30.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv32(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST31.json")
        self.assertEqual("The ID is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv33(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST32.json")
        self.assertEqual("The Localizer is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv34(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST33.json")
        self.assertEqual("The Localizer is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv35(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST34.json")
        self.assertEqual("The Localizer is not valid.", ome.exception.message)

    @freeze_time("2024-03-18")
    def test_nv36(self):
        mi_manager = HotelManager()
        self.ruta_json = HotelManager.RUTAARCHIVOJSON()
        with self.assertRaises(HotelManagementException) as ome:
            mi_roomKey = mi_manager.GUESTARRIVAL(self.ruta_json + "TestsSegundaFuncion/TEST35.json")
        self.assertEqual("The Localizer is not valid.", ome.exception.message)

if __name__ == '__main__':
    unittest.main()