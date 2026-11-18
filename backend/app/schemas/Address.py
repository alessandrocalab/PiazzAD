from pydantic import BaseModel, Field
from app.core.constants import ADDRESS_CITY_MAX_LEN, ADDRESS_CITY_MIN_LEN, ADDRESS_STREET_MAX_LEN, ADDRESS_STREET_MIN_LEN

class Address(BaseModel):
    street: str = Field(min_length=ADDRESS_CITY_MIN_LEN, max_length=ADDRESS_CITY_MAX_LEN)
    CAP: str = Field(pattern=r"^\d{5}$")  # Foreign CAP may have different pattern
    city: str = Field(min_length=ADDRESS_STREET_MIN_LEN, max_length=ADDRESS_STREET_MAX_LEN)
