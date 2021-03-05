from typing import Optional

from pydantic import BaseModel, Field, validator

from .reverse_geocoding import ReverseGeocodingModel as CoordinatesModel

allowed_units = ["kilometers", "meters", "miles"]


class GeoDistanceModel(BaseModel):
    geo_point1: CoordinatesModel
    geo_point2: CoordinatesModel
    result_in: Optional[str] = Field(
        "kilometers", description="Unit of result distance"
    )

    @validator("result_in")
    def validate_result_in(cls, value):
        if not value.lower() in allowed_units:
            raise ValueError("not a valid unit, options are " + ",".join(allowed_units))
        return value
