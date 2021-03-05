from fastapi import APIRouter

router = APIRouter(tags=["Geo Distance"])

from .geo_distance import *
