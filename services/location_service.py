# from models.location import Location

# from repository import location_repo
 
# async def create_location(location: Location):

#     return await location_repo.create(location)
 
# async def get_locations(country: str = None):

#     return await location_repo.get_all(country)
 
# async def update_location(country: str, city_id: str, location: Location):

#     return await location_repo.update(country, city_id, location)
 
# async def delete_location(country: str, city_id: str):

#     return await location_repo.delete(country, city_id)

# import boto3
# from models.location import Location

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('Locations')

# async def create_location(location: Location):
#     key = {'country': location.country, 'city_id': location.city_id}
#     if 'Item' in table.get_item(Key=key):
#         return {"message": "Item already exists"}, 409
#     table.put_item(Item=location.model_dump())
#     return {"message": "Item created successfully"}, 201

# async def get_locations(country: str = None):
#     if country:
#         res = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('country').eq(country))
#         items = res.get('Items', [])
#     else:
#         res = table.scan()
#         items = res.get('Items', [])
#     return items if items else {"message": "No data found"}, 200

# async def update_location(country: str, city_id: str, location: Location):
#     key = {'country': country, 'city_id': city_id}
#     if 'Item' not in table.get_item(Key=key):
#         return {"message": "Item not found"}, 404
#     if country != location.country or city_id != location.city_id:
#         return {"message": "country and city_id must match"}, 400
#     table.put_item(Item=location.model_dump())
#     return {"message": "Item updated successfully"}, 200

# async def delete_location(country: str, city_id: str):
#     key = {'country': country, 'city_id': city_id}
#     if 'Item' not in table.get_item(Key=key):
#         return {"message": "Item not found"}, 404
#     table.delete_item(Key=key)
#     return {"message": "Item deleted successfully"}, 200


# import boto3
# import os
# from models.location import Location

# dynamodb = boto3.resource(
#     'dynamodb',
#     region_name='us-east-1',
#     aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
#     aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
# )
# table = dynamodb.Table('Locations')

# async def create_location(location: Location):
#     try:
#         # Convert pincode to string if needed
#         location_dict = location.model_dump()
#         location_dict['pincode'] = str(location_dict['pincode'])
#         key = {'country': location.country, 'city_id': location.city_id}
#         if 'Item' in table.get_item(Key=key):
#             return {"message": "Item already exists"}, 409
#         table.put_item(Item=location_dict)
#         return {"message": "Item created successfully"}, 201
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def get_locations(country: str = None):
#     try:
#         if country:
#             res = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('country').eq(country))
#             items = res.get('Items', [])
#         else:
#             res = table.scan()
#             items = res.get('Items', [])
#         return items if items else {"message": "No data found"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def update_location(country: str, city_id: str, location: Location):
#     try:
#         location_dict = location.model_dump()
#         location_dict['pincode'] = str(location_dict['pincode'])
#         key = {'country': country, 'city_id': city_id}
#         if 'Item' not in table.get_item(Key=key):
#             return {"message": "Item not found"}, 404
#         if country != location.country or city_id != location.city_id:
#             return {"message": "country and city_id must match"}, 400
#         table.put_item(Item=location_dict)
#         return {"message": "Item updated successfully"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def delete_location(country: str, city_id: str):
#     try:
#         key = {'country': country, 'city_id': city_id}
#         if 'Item' not in table.get_item(Key=key):
#             return {"message": "Item not found"}, 404
#         table.delete_item(Key=key)
#         return {"message": "Item deleted successfully"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500


# import boto3
# import os
# from models.location import Location

# dynamodb = boto3.resource(
#     'dynamodb',
#     region_name='us-east-1',
#     aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
#     aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
# )
# table = dynamodb.Table('Locations')

# async def create_location(location: Location):
#     try:
#         key = {'country': location.country, 'city_id': location.city_id}
#         if 'Item' in table.get_item(Key=key):
#             return {"message": "Item already exists"}, 409
#         table.put_item(Item=location.model_dump())
#         return {"message": "Item created successfully"}, 201
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def get_locations(country: str = None):
#     try:
#         if country:
#             res = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('country').eq(country))
#             items = res.get('Items', [])
#         else:
#             res = table.scan()
#             items = res.get('Items', [])
#         return items if items else {"message": "No data found"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def update_location(country: str, city_id: str, location: Location):
#     try:
#         key = {'country': country, 'city_id': city_id}
#         if 'Item' not in table.get_item(Key=key):
#             return {"message": "Item not found"}, 404
#         if country != location.country or city_id != location.city_id:
#             return {"message": "country and city_id must match"}, 400
#         table.put_item(Item=location.model_dump())
#         return {"message": "Item updated successfully"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# async def delete_location(country: str, city_id: str):
#     try:
#         key = {'country': country, 'city_id': city_id}
#         if 'Item' not in table.get_item(Key=key):
#             return {"message": "Item not found"}, 404
#         table.delete_item(Key=key)
#         return {"message": "Item deleted successfully"}, 200
#     except Exception as e:
#         return {"message": f"Error: {str(e)}"}, 500

# import boto3
# import os
# from models.location import Location

# # Connect to AWS DynamoDB using environment variables
# dynamodb = boto3.resource(
#     'dynamodb',
#     region_name='us-east-1',
#     aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
#     aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
# )
# table = dynamodb.Table('Locations')

# async def create_location(location: Location):
#     key = {'country': location.country, 'city_id': location.city_id}
#     if 'Item' in table.get_item(Key=key):
#         return {"message": "Item already exists"}, 409
#     table.put_item(Item=location.model_dump())
#     return {"message": "Item created successfully"}, 201

# async def get_locations(country: str = None):
#     if country:
#         res = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('country').eq(country))
#         items = res.get('Items', [])
#     else:
#         res = table.scan()
#         items = res.get('Items', [])
#     return items if items else {"message": "No data found"}, 200

# async def update_location(country: str, city_id: str, location: Location):
#     key = {'country': country, 'city_id': city_id}
#     if 'Item' not in table.get_item(Key=key):
#         return {"message": "Item not found"}, 404
#     if country != location.country or city_id != location.city_id:
#         return {"message": "country and city_id must match"}, 400
#     table.put_item(Item=location.model_dump())
#     return {"message": "Item updated successfully"}, 200

# async def delete_location(country: str, city_id: str):
#     key = {'country': country, 'city_id': city_id}
#     if 'Item' not in table.get_item(Key=key):
#         return {"message": "Item not found"}, 404
#     table.delete_item(Key=key)
#     return {"message": "Item deleted successfully"}, 200

from models.location import Location
from repository import location_repo as location_repository
 
async def create_location(location: Location):
    key = {'country': location.country, 'city_id': location.city_id}
    res = await location_repository.get_item(key)
    if 'Item' in res:
        return {"message": "Item already exists"}, 409
    await location_repository.put_item(location.model_dump())
    return {"message": "Item created successfully"}, 201
 
async def get_locations(country: str = None):
    if country:
        res = await location_repository.query_by_country(country)
        items = res.get('Items', [])
    else:
        res = await location_repository.scan_all()
        items = res.get('Items', [])
    return items if items else {"message": "No data found"}, 200
 
async def update_location(country: str, city_id: str, location: Location):
    key = {'country': country, 'city_id': city_id}
    res = await location_repository.get_item(key)
    if 'Item' not in res:
        return {"message": "Item not found"}, 404
    if country != location.country or city_id != location.city_id:
        return {"message": "country and city_id must match"}, 400
    await location_repository.put_item(location.model_dump())
    return {"message": "Item updated successfully"}, 200
 
async def delete_location(country: str, city_id: str):
    key = {'country': country, 'city_id': city_id}
    res = await location_repository.get_item(key)
    if 'Item' not in res:
        return {"message": "Item not found"}, 404
    await location_repository.delete_item(key)
    return {"message": "Item deleted successfully"}, 200