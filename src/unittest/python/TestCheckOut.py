import os
import json
import unittest
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException

class MyTestCase(unittest.TestCase):
    """CLASE QUE COMPRUEBA EL MÉTODO 3: FUNCION CHECKOUT"""