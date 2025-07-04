
# from fastapi import FastAPI
# from routes.location_routes import router as location_router
#  # ROUTES IS MY FOLDER, LOCATION_ROUTES IS THE FILE NAME,ROUTER IS THE VARIABLE NAME and location_router is the alias
# app = FastAPI()
# app.include_router(location_router) # Include the auth routes

# from fastapi import FastAPI
# from routes.location_routes import router as location_router
# from dotenv import load_dotenv
# import os

# load_dotenv()  # Load environment variables from .env
# app = FastAPI()
# app.include_router(location_router)

from fastapi import FastAPI
from routes.location_routes import router as location_router
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env from root directory
app = FastAPI()
app.include_router(location_router)
















# @app.post("/auth/token")
# async def dummy_token():
#     return {"access_token": "your_token_here", "token_type": "bearer"}

 
#  title="HMS API",
    # description="Use the 🔒 button to authorize with your Bearer JWT token.",
    # version="1.0.0"

