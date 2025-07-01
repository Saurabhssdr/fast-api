from fastapi import APIRouter, Query
# from fastapi.params import Depends

from models.location import Location

from services import location_service

# from auth.oauth2 import get_current_user 
 
# router = APIRouter()
router = APIRouter(
    # dependencies=[Depends(get_current_user)]  # 🔒 protect all endpoints in this router
)
 
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

# from fastapi import APIRouter, Depends, HTTPException

# from models.location import Location

# from services.location_service import *

# from auth.oauth2 import oauth2_scheme

# from auth.oauth2 import get_current_user
 
# router = APIRouter(prefix="/locations", tags=["Locations"])
 
# @router.post("/")

# async def create(location: Location, token: str = Depends(oauth2_scheme)):

#     return await create_location_service(location, token)
 
# @router.get("/")

# async def get_all(country: str = None, token: str = Depends(oauth2_scheme)):

#     return await get_all_locations_service(country, token)
 
# @router.put("/")

# async def update(country: str, city_id: str, location: Location, token: str = Depends(oauth2_scheme)):

#     try:

#         return await update_location_service(country, city_id, location, token)

#     except ValueError as ve:

#         raise HTTPException(status_code=400, detail=str(ve))
 
# @router.delete("/")

# async def delete(country: str, city_id: str, token: str = Depends(oauth2_scheme)):

#     return await delete_location_service(country, city_id, token)

# @router.get("/secure")

# async def secured_data(user: dict = Depends(get_current_user)):

#     return {"message": f"Hello {user['sub']}, role: {user['role']}"}


# from fastapi import APIRouter, Depends, HTTPException

# from models.location import Location

# from services.location_service import *

# from auth.oauth2 import get_current_user
 
# router = APIRouter(prefix="/locations", tags=["Locations"])
 
# @router.post("/")

# async def create(location: Location, user=Depends(get_current_user)):

#     return await create_location_service(location, user["token"])
 
# @router.get("/")

# async def get_all(country: str = None, user=Depends(get_current_user)):

#     return await get_all_locations_service(country, user["token"])
 
# @router.put("/")

# async def update(country: str, city_id: str, location: Location, user=Depends(get_current_user)):

#     try:

#         return await update_location_service(country, city_id, location, user["token"])

#     except ValueError as ve:

#         raise HTTPException(status_code=400, detail=str(ve))
 
# @router.delete("/")

# async def delete(country: str, city_id: str, user=Depends(get_current_user)):

#     return await delete_location_service(country, city_id, user["token"])

# from fastapi import APIRouter, Depends, HTTPException

# from models.location import Location

# from services.location_service import *

# from auth.oauth2 import get_current_user
 
# router = APIRouter(prefix="/locations", tags=["Locations"])
 
# @router.post("/")

# async def create(location: Location, user=Depends(get_current_user)):

#     return await create_location_service(location, token=user["sub"])
 
# @router.get("/")

# async def get_all(country: str = None, user=Depends(get_current_user)):

#     return await get_all_locations_service(country, token=user["sub"])
 
# @router.put("/")

# async def update(country: str, city_id: str, location: Location, user=Depends(get_current_user)):

#     try:

#         return await update_location_service(country, city_id, location, token=user["sub"])

#     except ValueError as ve:

#         raise HTTPException(status_code=400, detail=str(ve))
 
# @router.delete("/")

# async def delete(country: str, city_id: str, user=Depends(get_current_user)):

#     return await delete_location_service(country, city_id, token=user["sub"])

 

 
 
 