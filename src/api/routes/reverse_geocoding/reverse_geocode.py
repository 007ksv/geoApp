from src.models import GeocodingModel, ReverseGeocodingModel
from src.utils.address import get_reverse
from src.utils.response import create_response

from . import router


@router.post("/reverse")
def get_reverse_geocoding_details(coordinates: ReverseGeocodingModel):
    coords = (coordinates.latitude, coordinates.longitude)
    address = get_reverse(coords)
    if address:
        response = GeocodingModel(**address)
        return create_response(success=True, data=response.dict())
    return create_response(success=True, data={})
