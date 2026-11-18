# TODO adapt to database implementation
from pydantic import BaseModel

from app.schemas.Address import AddressResponse


class BillboardResponse(BaseModel):
    name: str
    status: str
    address: AddressResponse
