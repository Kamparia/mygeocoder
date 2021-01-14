from fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()

# forward geocoding
@router.get("/forward", name="Forward Geocoding", description="Returns latitude and longitude of a given address.")
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