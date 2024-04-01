from datetime import datetime
class HotelCheckout:
    """Clase para controlar las salidas del hotel"""

    def __init__(self, strRoomKey):
        self.__strRoomKey = strRoomKey
        self.__intFechaSalida = datetime.today().date()

    def __signature_string(self):
        """Crea las claves para guardar en el archivo json"""
        return "{room_key:" + self.__strRoomKey + ", fecha_salida:" + self.__intFechaSalida + "}"

    @property
    def strRoomKey(self):
        return self.__strRoomKey

    @strRoomKey.setter
    def strRoomKey(self, valor):
        self.__strRoomKey = valor

    @property
    def intFechaSalida(self):
        return self.__intFechaSalida