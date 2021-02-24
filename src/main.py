from fastapi import FastAPI

from .api.routes import main_router

app = FastAPI(debug=True)


@app.get("/")
def home():
    return {"message": "Welcome to geoApp"}


app.include_router(main_router, prefix="/v1")
