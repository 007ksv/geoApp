from src.models import GeocodingDetailModel, GeocodingModel
from src.utils.address import get_address_details
from src.utils.response import create_response

from . import router


@router.post("/address-detail")
def get_address_detail(adress: GeocodingModel):
    addr = adress.address
    address_detail = get_address_details(addr)
    if address_detail:
        response = GeocodingDetailModel(**address_detail)
        return create_response(success=True, data=response.dict())
    return create_response(success=True, data={})
