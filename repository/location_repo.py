import boto3
import os
from dotenv import load_dotenv
from models.location import Location
from boto3.dynamodb.conditions import Key

load_dotenv()  # Load environment variables from .env

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
 
# Setup DynamoDB connection
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
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
