import json

from .HotelManagementException import HOTELMANAGMENTEXCEPTION

from .HotelReservation import HOTELRESERVATION

class HOTELMANAGER:
    def __init__( self ):
        pass

    def VALIDATECREDITCARD( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def READDATAFROMJSON( self, strFi ):

        try:
            with open( strFi ) as f:
                strData = json.load( f )
        except FileNotFoundError as e:
            raise HOTELMANAGMENTEXCEPTION("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HOTELMANAGMENTEXCEPTION("JSON Decode Error - Wrong JSON Format") from e


        try:
            strC = strData["CreditCard"]
            strP = strData["phoneNumber"]
            req = HOTELRESERVATION(IDCARD="12345678Z",creditcardNumb=strC,nAMeAndSURNAME="John Doe",phonenumber=strP,room_type="single",numdays=3)
        except KeyError as e:
            raise HOTELMANAGMENTEXCEPTION("JSON Decode Error - Invalid JSON Key") from e
        if not self.VALIDATECREDITCARD(c):
            raise HOTELMANAGMENTEXCEPTION("Invalid credit card number")

        # Close the file
        return req