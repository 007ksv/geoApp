from fastapi import APIRouter

from . import geo_coding, reverse_geocoding

main_router = APIRouter()

main_router.include_router(geo_coding.router)
main_router.include_router(reverse_geocoding.router)
