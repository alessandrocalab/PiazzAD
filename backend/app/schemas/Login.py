from pydantinc import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str