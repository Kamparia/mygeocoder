from fastapi import FastAPI
from routers import router

# fastapi app
app = FastAPI(
    title="MyGeocoder",
    description="A simple Geocoding API Service built with FastAPI",
    version="0.1"
)

app.include_router(router)


# uvicorn main:app --reload