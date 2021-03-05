from src.models import GeoDistanceModel
from src.utils.geo_distance import calculate_geo_distance
from src.utils.response import create_response

from . import router


@router.post("/geo-distance")
def get_geo_distance(coords: GeoDistanceModel):
    result_in = coords.result_in
    point1 = (coords.geo_point1.latitude, coords.geo_point1.longitude)
    point2 = (coords.geo_point2.latitude, coords.geo_point2.longitude)
    distance = calculate_geo_distance(point1, point2, result_in)
    response = {"result": distance}
    return create_response(True, data=response)
