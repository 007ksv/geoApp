from fastapi import FastAPI

from .models import AddressDetailModel, AddressModel, CoordinatesModel
from .utils.address import get_address_details, get_reverse

app = FastAPI(debug=True)


def create_response(success, data):
    if success:
        res = {"success": success, "data": data}
    else:
        res = {"success": success, "data": {}}
    return res


@app.post("/address-detail")
def get_address_detail(adress: AddressModel):
    addr = adress.address
    address_detail = get_address_details(addr)
    if address_detail:
        response = AddressDetailModel(**address_detail)
        return create_response(success=True, data=response)
    return create_response(success=True, data={})


@app.post("/reverse")
def get_reverse_details(coordinates: CoordinatesModel):
    coords = (coordinates.latitude, coordinates.longitude)
    address = get_reverse(coords)
    if address:
        response = AddressModel(**address)
        return create_response(success=True, data=response.dict())
    return create_response(success=True, data={})
