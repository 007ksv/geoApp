from fastapi import FastAPI

from .models import GeocodingDetailModel, GeocodingModel, ReverseGeocodingModel
from .utils.address import get_address_details, get_reverse
from .utils.response import create_response

app = FastAPI(debug=True)


@app.post("/address-detail")
def get_address_detail(adress: GeocodingModel):
    addr = adress.address
    address_detail = get_address_details(addr)
    if address_detail:
        response = GeocodingDetailModel(**address_detail)
        return create_response(success=True, data=response.dict())
    return create_response(success=True, data={})


@app.post("/reverse")
def get_reverse_geocoding_details(coordinates: ReverseGeocodingModel):
    coords = (coordinates.latitude, coordinates.longitude)
    address = get_reverse(coords)
    if address:
        response = GeocodingModel(**address)
        return create_response(success=True, data=response.dict())
    return create_response(success=True, data={})
