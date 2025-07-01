# from fastapi import FastAPI, HTTPException, Query
# from pydantic import BaseModel
# import httpx

# app = FastAPI()

# API_URL = "https://qvcxemu23i.execute-api.us-east-1.amazonaws.com/prod/Locations"


# jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIn0.xob4dHm4rikTbAyqBaYtVSRzeO7Sz3chteZBjBoVmM0"

# class Location(BaseModel):
#     country: str
#     city_id: str
#     city_name: str
#     pincode: int
#     state_name: str


# # Create operation
# @app.post("/locations", tags=["Create APIs"])
# async def create_location(location: Location):
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.post(
#                 API_URL,
#                 json=location.model_dump(),
#                 headers=headers
#             )
#             response.raise_for_status()
#             return response.json()
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# # Read operation
# @app.get("/locations", tags=["Read APIs"])
# async def get_locations(
#     country: str = Query(default=None)
# ):
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }
#     params = {}
#     if country:
#         params["country"] = country
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.get(API_URL, params=params, headers=headers)
#             response.raise_for_status()
#             return response.json()
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# # Update operation
# @app.put("/locations", tags=["Update APIs"])
# async def update_location(country: str, city_id: str, location: Location):
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }
#     if country != location.country or city_id != location.city_id:
#         raise HTTPException(status_code=400, detail="Country and city_id in path must match the body")
             
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.put(
#                 API_URL,
#                 json=location.model_dump(),
#                 headers=headers
#             )
#             response.raise_for_status()   
#             return response.json()
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Delete operation
# @app.delete("/locations", tags=["Delete APIs"])
# async def delete_location(country: str, city_id: str):
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }
#     try:
#         async with httpx.AsyncClient() as client:
#             response = await client.delete(
#                 API_URL,
#                 params={"country": country, "city_id": city_id},
#                 headers=headers
#             )
#             response.raise_for_status()
#             return response.json()
#     except httpx.HTTPStatusError as e:
#         raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI
from routes.location_routes import router as location_router
 # ROUTES IS MY FOLDER, LOCATION_ROUTES IS THE FILE NAME,ROUTER IS THE VARIABLE NAME and location_router is the alias
app = FastAPI()

#  title="HMS API",
    # description="Use the 🔒 button to authorize with your Bearer JWT token.",
    # version="1.0.0"
app.include_router(location_router) # Include the auth routes

# @app.post("/auth/token")
# async def dummy_token():
#     return {"access_token": "your_token_here", "token_type": "bearer"}

 

# from fastapi import FastAPI
# from routes import location_route 
 
# app = FastAPI()
# app.include_router(location_route.router)
 
# @app.post("/auth/token")
# async def dummy_token():
#     return {"access_token": "your_token_here", "token_type": "bearer"}
