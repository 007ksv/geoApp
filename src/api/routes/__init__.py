from fastapi import APIRouter

from . import geo_coding, geo_distance, reverse_geocoding

main_router = APIRouter()

main_router.include_router(geo_coding.router)
main_router.include_router(reverse_geocoding.router)
main_router.include_router(geo_distance.router)
