import unittest
from UC3MTravel import HotelReservation
import json
import os
from pathlib import Path

class TestsReservation(unittest.TestCase):
    def test_room_reservation_valid1_complete(self):
        file_store = str(Path.home()) + "/PycharmProjects/G842024.T10.EG2/test.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        with open(file_store,"r", encoding="utf-8", newline="" ) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item("_HotelReservation__idcard") == "12345678P":
                found = True
        self.assertTrue(found)




if __name__ == '__main__':
    unittest.main()
