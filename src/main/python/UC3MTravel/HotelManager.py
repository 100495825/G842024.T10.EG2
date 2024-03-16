import json
from .HotelManagementException import HOTELMANAGMENT
from .HotelReservation import HotelReservation


class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID4
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HOTELMANAGMENT("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HOTELMANAGMENT("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",
                                   phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HOTELMANAGMENT("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HOTELMANAGMENT("Invalid credit card number")

        # Close the file
        return req