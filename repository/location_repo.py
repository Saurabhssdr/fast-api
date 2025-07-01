import httpx

from fastapi import HTTPException

from models.location import Location
 
API_URL = "https://qvcxemu23i.execute-api.us-east-1.amazonaws.com/prod/Locations"

jwt_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIn0.xob4dHm4rikTbAyqBaYtVSRzeO7Sz3chteZBjBoVmM0"
 
headers = {

    "Authorization": jwt_token,

    "Content-Type": "application/json"

}
 
async def create(location: Location):

    async with httpx.AsyncClient() as client:

        response = await client.post(API_URL, json=location.model_dump(), headers=headers)

        response.raise_for_status()

        return response.json()
 
async def get_all(country: str = None):

    async with httpx.AsyncClient() as client:

        response = await client.get(API_URL, params={"country": country} if country else {}, headers=headers)

        response.raise_for_status()

        return response.json()
 
async def update(country: str, city_id: str, location: Location):

    if country != location.country or city_id != location.city_id:

        raise HTTPException(status_code=400, detail="country and city_id must match")
 
    async with httpx.AsyncClient() as client:

        response = await client.put(API_URL, json=location.model_dump(), headers=headers)

        response.raise_for_status()

        return response.json()
 
async def delete(country: str, city_id: str):

    async with httpx.AsyncClient() as client:

        response = await client.delete(API_URL, params={"country": country, "city_id": city_id}, headers=headers)

        response.raise_for_status()

        return response.json()

# import httpx

# from models.location import Location
 
# API_URL = "https://qvcxemu23i.execute-api.us-east-1.amazonaws.com/prod/Locations"
 
# async def create_location(location: Location, token: str):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.post(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def get_all_locations(country: str = None, token: str = ""):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.get(API_URL, params={"country": country} if country else {}, headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def update_location(country: str, city_id: str, location: Location, token: str):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.put(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def delete_location(country: str, city_id: str, token: str):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.delete(API_URL, params={"country": country, "city_id": city_id}, headers=headers)

#         response.raise_for_status()

#         return response.json()

# import httpx

# from models.location import Location
 
# API_URL = "https://qvcxemu23i.execute-api.us-east-1.amazonaws.com/prod/Locations"
 
# async def create_location(location: Location, token: str):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.post(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def get_all_locations(country: str, token: str):

#     headers = {"Authorization": f"Bearer {token}"}

#     params = {"country": country} if country else {}

#     async with httpx.AsyncClient() as client:

#         response = await client.get(API_URL, params=params, headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def update_location(location: Location, token: str):

#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     async with httpx.AsyncClient() as client:

#         response = await client.put(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def delete_location(country: str, city_id: str, token: str):

#     headers = {"Authorization": f"Bearer {token}"}

#     async with httpx.AsyncClient() as client:

#         response = await client.delete(API_URL, params={"country": country, "city_id": city_id}, headers=headers)

#         response.raise_for_status()

#         return response.json()

 

 
 