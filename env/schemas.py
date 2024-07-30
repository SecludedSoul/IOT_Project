from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class RequestUser(BaseModel):
    parameter: UserSchema

class ResponseUser(GenericModel, Generic[T]):
    code: int
    message: str
    status: str
    result: Optional[T] = None
