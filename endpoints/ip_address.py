from fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()

# ip_address geocoding
@router.get("/ip_address", name="Geocode IP Address", description="Returns address and geographical coordinates of an IP.")
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