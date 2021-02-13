from pydantic import BaseModel


class AddressModel(BaseModel):
    address: str


class CoordinatesModel(BaseModel):
    latitude: float
    longitude: float


class AddressDetailModel(BaseModel):
    address: str
    coordinates: CoordinatesModel
