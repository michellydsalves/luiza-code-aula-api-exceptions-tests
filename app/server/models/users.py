from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str
    age: int
    cpf: str
    email: EmailStr
    obs: Optional[str]
    

class UserSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    cpf: str = Field(...)
    email: EmailStr = Field(...)
    obs: Optional[str] = Field()
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Michelly Alves",
                "age": 18,
                "cpf": "00000000",
                "email": "michellydsalves@gmail.com"
            }
        }