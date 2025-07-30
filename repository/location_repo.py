
# import httpx

# from fastapi import HTTPException

# from models.location import Location
 
# API_URL = "https://qvcxemu23i.execute-api.us-east-1.amazonaws.com/prod/Locations"

# jwt_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIn0.xob4dHm4rikTbAyqBaYtVSRzeO7Sz3chteZBjBoVmM0"
 
# headers = {

#     "Authorization": jwt_token,

#     "Content-Type": "application/json"

# }
 
# async def create(location: Location):

#     async with httpx.AsyncClient() as client:

#         response = await client.post(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def get_all(country: str = None):

#     async with httpx.AsyncClient() as client:

#         response = await client.get(API_URL, params={"country": country} if country else {}, headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def update(country: str, city_id: str, location: Location):

#     if country != location.country or city_id != location.city_id:

#         raise HTTPException(status_code=400, detail="country and city_id must match")
 
#     async with httpx.AsyncClient() as client:

#         response = await client.put(API_URL, json=location.model_dump(), headers=headers)

#         response.raise_for_status()

#         return response.json()
 
# async def delete(country: str, city_id: str):

#     async with httpx.AsyncClient() as client:

#         response = await client.delete(API_URL, params={"country": country, "city_id": city_id}, headers=headers)

#         response.raise_for_status()

#         return response.json()

# import boto3
# import os
# from dotenv import load_dotenv
# from models.location import Location
# from boto3.dynamodb.conditions import Key

# load_dotenv()  # Load environment variables from .env

# aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
# region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
            
                                  
 
# # Setup DynamoDB connection
# dynamodb = boto3.resource(
#     'dynamodb',
#     region_name='us-east-1',
#     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
#     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
# )
# table = dynamodb.Table('Locations')
 
# async def get_item(key: dict):
#     return table.get_item(Key=key)
 
# async def put_item(item: dict):
#     table.put_item(Item=item)
 
# async def delete_item(key: dict):
#     table.delete_item(Key=key)
 
# async def query_by_country(country: str):
#     return table.query(KeyConditionExpression=Key('country').eq(country))
 
# async def scan_all():
#     return table.scan()
 

import boto3
from boto3.dynamodb.conditions import Key
 
# No need to load .env or use os.getenv

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('LocationsTerraform')
 
async def get_item(key: dict):
    return table.get_item(Key=key)
 
async def put_item(item: dict):
    table.put_item(Item=item)
 
async def delete_item(key: dict):
    table.delete_item(Key=key)
 
async def query_by_country(country: str):
    return table.query(KeyConditionExpression=Key('country').eq(country))
 
async def scan_all():
    return table.scan()
