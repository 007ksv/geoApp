from fastapi import APIRouter

router = APIRouter(tags=["Reverse geocoding"])

from .reverse_geocode import *
