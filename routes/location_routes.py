# from fastapi import APIRouter, Query

# from models.location import Location

# from services import location_service

# router = APIRouter()
 
# @router.post("/locations", tags=["Create APIs"])

# async def create_location_route(location: Location):  

#     return await location_service.create_location(location)
 
# @router.get("/locations", tags=["Read APIs"])

# async def get_locations_route(country: str = Query(default=None)):

#     return await location_service.get_locations(country)
 
# @router.put("/locations", tags=["Update APIs"])

# async def update_location_route(country: str, city_id: str, location: Location):

#     return await location_service.update_location(country, city_id, location)
 
# @router.delete("/locations", tags=["Delete APIs"])

# async def delete_location_route(country: str, city_id: str):

#     return await location_service.delete_location(country, city_id)


from fastapi import APIRouter, Query
from models.location import Location
from services import location_service
 
router = APIRouter()
 
@router.post("/locations", tags=["Create APIs"])
async def create_location_route(location: Location):
    return await location_service.create_location(location)
 
@router.get("/locations", tags=["Read APIs"])
async def get_locations_route(country: str = Query(default=None)):
    return await location_service.get_locations(country)
 
@router.put("/locations", tags=["Update APIs"])
async def update_location_route(country: str, city_id: str, location: Location):
    return await location_service.update_location(country, city_id, location)
 
@router.delete("/locations", tags=["Delete APIs"])
async def delete_location_route(country: str, city_id: str):
    return await location_service.delete_location(country, city_id)










































#2  from fastapi.params import Depends
#8 from auth.oauth2 import get_current_user
#in API Router() dependencies=[Depends(get_current_user)]  # 🔒 protect all endpoints in this router