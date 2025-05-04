from pydantic import BaseModel, EmailStr
from typing import Optional


# CREATE OWNER
class OwnerCreate(BaseModel):
    name : str
    email : EmailStr
    mobile : Optional[int] = None  # Now it's optional

#------------------------------------------------------------------------------------------------------------------

# UPDATE OWNER 
class OwnerUpdate(BaseModel):
    name : Optional[str]
    email : Optional[EmailStr]
    mobile : Optional[int]