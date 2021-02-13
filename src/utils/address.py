from geopy.geocoders import Nominatim


def get_address_details(address: str):
    try:
        locator = Nominatim(user_agent="Keshav")
        address_detail = locator.geocode(address)
        res = {}
        if address_detail:
            res["address"] = address_detail.address
            res["coordinates"] = {
                "latitude": address_detail.latitude,
                "longitude": address_detail.longitude,
            }
            return res
        else:
            return None
    except Exception as e:
        print(e)


def get_reverse(coords: tuple):
    try:
        locator = Nominatim(user_agent="keshav")
        address = locator.reverse(coords)
        res = {}
        if address:
            res["address"] = address.address
            return res
        else:
            None
    except Exception as e:
        print(e)
