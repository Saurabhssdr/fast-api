from models.location import Location

from repository import location_repo
 
async def create_location(location: Location):

    return await location_repo.create(location)
 
async def get_locations(country: str = None):

    return await location_repo.get_all(country)
 
async def update_location(country: str, city_id: str, location: Location):

    return await location_repo.update(country, city_id, location)
 
async def delete_location(country: str, city_id: str):

    return await location_repo.delete(country, city_id)

# from models.location import Location
# from repository.location_repo import *
 
# async def create_location_service(location: Location, token: str):
#     return await create_location(location, token)
 
# async def get_all_locations_service(country: str, token: str):
#     return await get_all_locations(country, token)
 
# async def update_location_service(country: str, city_id: str, location: Location, token: str):
#     if country != location.country or city_id != location.city_id:
#         raise ValueError("country and city_id must match")
#     return await update_location(country, city_id, location, token)
 
# async def delete_location_service(country: str, city_id: str, token: str):
#     return await delete_location(country, city_id, token)

# from models.location import Location
# from repository.location_repo import *
 
# async def create_location_service(location: Location, token: str):
#     return await create_location(location, token)
 
# async def get_all_locations_service(country: str, token: str):
#     return await get_all_locations(country, token)
 
# async def update_location_service(country: str, city_id: str, location: Location, token: str):
#     if country != location.country or city_id != location.city_id:
#         raise ValueError("country and city_id must match")
#     return await update_location(location, token)
 
# async def delete_location_service(country: str, city_id: str, token: str):
#     return await delete_location(country, city_id, token)