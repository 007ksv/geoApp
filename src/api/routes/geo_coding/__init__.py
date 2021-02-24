from fastapi import APIRouter

router = APIRouter(tags=["Geo coding"])

from .geo_code import *
