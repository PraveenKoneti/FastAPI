from pydantic import BaseModel, EmailStr
from typing import Optional

# CREATE USER
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    mobile: int
    userType: str
    password: str

#---------------------------------------------------------------------------------------------------------------

# UPDATE USER
class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    mobile: Optional[int]
    userType: Optional[str]
    password: Optional[str]