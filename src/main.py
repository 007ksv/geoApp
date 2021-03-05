from fastapi import FastAPI

from .api.routes import main_router
from .utils.response import create_response

app = FastAPI(debug=True)


@app.get("/v1/")
def home():
    return create_response(True, data={"message": "Welcome to geoApp"})


app.include_router(main_router, prefix="/v1")
