from pydantic import BaseModel, validator


class ReverseGeocodingModel(BaseModel):
    latitude: float
    longitude: float

    @validator("latitude")
    def validate_latitude(cls, value):
        if not (value >= -90 and value <= 90):
            raise ValueError("not a valid latitude")

        return value

    @validator("longitude")
    def validate_longitude(cls, value):
        if not (value >= -180 and value <= 180):
            raise ValueError("not a valid longitude")

        return value
