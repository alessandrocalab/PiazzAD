from pydantic import BaseModel, EmailStr, field_validator, Field, model_validator

from app.core.constants import PASSWORD_MIN_LEN, PASSWORD_MAX_LEN
from app.core.password_validator import validate_password


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=PASSWORD_MIN_LEN , max_length=PASSWORD_MAX_LEN )


class ChangePasswordRequest(BaseModel):
    currentPassword: str 
    new_password: str
    new_password_ver: str

    @field_validator("new_password", "new_password_ver")
    @classmethod
    def check_password(cls, password: str)->str:
        return validate_password(password)

    @model_validator(mode="after") #mode=affter mean that the validation is executed after the  field validator
    def check_password_match(self):
        if self.new_password != self.new_password_ver:
            raise ValueError("Password do not match")
        
        return self



class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=PASSWORD_MIN_LEN , max_length=PASSWORD_MAX_LEN )

    @field_validator("password")
    @classmethod
    def check_password(cls, password: str)->str:
        return validate_password(password)