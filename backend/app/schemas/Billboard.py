# TODO adapt to database implementation
from pydantic import BaseModel, Field

from app.core.constants import BILLBOARD_NAME_MIN_NAME_LEN, BILLBOARD_NAME_MAX_NAME_LEN
from app.schemas.Address import Address
from app.enums.BillboardStatus import BillboardStatus


class BillboardResponse(BaseModel):
    name: str = Field(
            min_length=BILLBOARD_NAME_MIN_NAME_LEN,
            max_length=BILLBOARD_NAME_MAX_NAME_LEN
        ) 
    status: BillboardStatus
    address: Address


class BillboardCreate(BaseModel):
    name:str = Field(
            min_length=BILLBOARD_NAME_MIN_NAME_LEN,
            max_length=BILLBOARD_NAME_MAX_NAME_LEN
        ) 
    address: Address


class BillboardUpdate(BaseModel):
    name:str | None = Field(
                min_length=BILLBOARD_NAME_MIN_NAME_LEN,
                max_length=BILLBOARD_NAME_MAX_NAME_LEN,
                default=None
        ) 
    status: BillboardStatus | None = None #optional
    address: Address | None = None 