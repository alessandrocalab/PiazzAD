from pydantic import BaseModel, Field


class AddressResponse(BaseModel):
    street: str
    CAP: str = Field(pattern=r"^\d{5}$")  # Foreign CAP may have different pattern
    city: str
