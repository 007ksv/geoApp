from pydantic import BaseModel

from .reverse_geocoding import ReverseGeocodingModel


class GeocodingModel(BaseModel):
    address: str


class GeocodingDetailModel(BaseModel):
    address: str
    coordinates: ReverseGeocodingModel
