
from typing import List, Optional
from pydantic import BaseModel

class UserAddressModel(BaseModel):
    
    id: Optional[int]
    street: str
    number: Optional[str] = None
    zipcode: Optional[str] = None
    neighborhood: Optional[str] = None
    complement: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    lat: Optional[str] = None
    lng: Optional[str] = None
    system_id: Optional[str] = None
    delivery_fee: Optional[str] = None

    class Config:
        orm_mode = True


class OrderUserModel(BaseModel):
    
    id: Optional[int]
    name: str
    phone: str
    formatted_telephone: str
    email: str
    document: str
    user_id: str
    address: List[UserAddressModel]

    @classmethod
    def dict_types(self):
        return {
            "address":UserAddressModel
        }
    
    class Config:
        orm_mode = True

# class OrderItemsModel(BaseModel):
    
#     id: Optional[int]
#     amount: int
#     comments: str
#     name: str
#     price: str

class CreateOrderModel(BaseModel):

    is_from_admin: bool
    is_from_phone_central: bool
    formatted_status: str
    order_id: Optional[str] = None
    total: str
    created: str
    type: str
    is_online_payment: bool
    is_takeout: bool
    payment: Optional[str] = ""
    user: OrderUserModel
    # items: List[OrderItemsModel]
    paymentOnlineCreditCardLastNumbers: Optional[str]

    @classmethod
    def dict_types(self):
        return {
            "user":OrderUserModel
        }

class OrderModel(BaseModel):

    id: int
    is_from_admin: bool
    is_from_phone_central: bool
    formatted_status: str
    order_id: Optional[str] = None
    total: str
    created: str
    type: str
    is_online_payment: bool
    is_takeout: bool
    payment: str
    user: OrderUserModel
    # items: List[OrderItemsModel]
    paymentOnlineCreditCardLastNumbers: Optional[str]

    class Config:
        orm_mode = True

    @classmethod
    def dict_types(self):
        return {
            "user":OrderUserModel
        }

class ListCreateOrderModel(BaseModel):
    
    orders:List[CreateOrderModel]