from typing import Optional
from pydantic import BaseModel

class CreateUserModel(BaseModel):

    mac: str
    name: str
    email: str
    key: str
    teste: str
    validity: str

class UserQrcodeModel(BaseModel):
    
    qrcode: str
    
    class Config:
        orm_mode = True

class UserModel(BaseModel):

    id:int
    mac: str
    name: str
    email: str
    key: str
    teste: str
    validity: str
    qrcode: Optional[UserQrcodeModel] = None

    class Config:
        orm_mode = True