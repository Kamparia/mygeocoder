from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
import geocoder

# fastapi app
app = FastAPI(
    title="MyGeocoder",
    description="A simple Geocoding API Service built with FastAPI",
    version="0.1"
)


def ResponseModel(data, message):
    return JSONResponse(
        status_code=200, 
        content={"code": 200, "status": message, "data": data}
    )    


def ErrorResponseModel(code, message):
    return JSONResponse(
        status_code=code, 
        content={"code": code, "message": message}
    )


# home page
@app.get("/", name="Home Page", description="API Documentation Page.")
async def main():
    """API Documentation Page."""
    return RedirectResponse(url="/docs/")


# forward geocoding
@app.get("/forward", name="Forward Geocoding", description="Returns latitude and longitude of a given address.")
async def forward(address: str):
    """Returns latitude and longitude of a given address."""
    try:
        geolocator = geocoder.osm(address)
        address = geolocator.json['raw']['display_name']
        lat = geolocator.json['raw']['lat']
        lon = geolocator.json['raw']['lon']
        data = {
            "source": "OSM",
            "longitude": lat,
            "latitude": lon, 
            "address": address
        }
        return ResponseModel(data, "success")
    except Exception:
        return ErrorResponseModel(503, "Internal Server Error.")


# reverse geocoding
@app.get("/reverse", name="Reverse Geocoding", description="Returns the address of given geographical coordinates.")
async def reverse(lat: float, lon: float):
    """Returns the address of given geographical coordinates."""
    try:
        geolocator = geocoder.osm([lat, lon], method='reverse')
        address = geolocator.json['raw']['display_name']
        data = {
            "source": "OSM",
            "longitude": lat,
            "latitude": lon, 
            "address": address
        }
        return ResponseModel(data, "success")
    except Exception:
        return ErrorResponseModel(503, "Internal Server Error.")


# ip_address geocoding
@app.get("/ip_address", name="Geocode IP Address", description="Returns address and geographical coordinates of an IP.")
async def ip_address(ip: str):
    """Returns address and geographical coordinates of an IP."""
    try:
        geolocator = geocoder.ip(ip)
        coord = geolocator.json['raw']['loc'].split(",")
        lat, lon = coord[0], coord[1]
        geolocator = geocoder.osm([lat, lon], method='reverse')
        address = geolocator.json['raw']['display_name']
        data = {
            "source": "OSM",
            "longitude": lat,
            "latitude": lon,
            "address": address
        }
        return ResponseModel(data, "success")
    except Exception:
        return ErrorResponseModel(400, "Invalid IP_Address input.")


# uvicorn main:app --reload