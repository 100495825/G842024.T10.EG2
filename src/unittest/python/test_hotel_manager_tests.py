import unittest


class TestHotelManager(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
    #copiado de la profe
    def test_room_reservation_valid(self):
        my_reservation= HotelManager()
        value=my_reservation.room_reservation("5105105105105100", "jose lopez", "12345678", "912345678", "single",
                                              ) #aquí continuaba pero es una prisas