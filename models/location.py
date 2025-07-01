from pydantic import BaseModel
 
class Location(BaseModel):
    country: str
    city_id: str
    city_name: str
    pincode: int
    state_name: str
    