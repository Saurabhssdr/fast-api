import boto3
from boto3.dynamodb.conditions import Key
 
# No need to load .env or use os.getenv
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Locations')
 
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
