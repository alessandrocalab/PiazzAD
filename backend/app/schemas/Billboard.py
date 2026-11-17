#TODO adapt to database implementation
from pydantic import BaseModel
from app.schemas.Address import Address

class BillboardResponse(BaseModel):
    name: str
    status: str
    addres: Address