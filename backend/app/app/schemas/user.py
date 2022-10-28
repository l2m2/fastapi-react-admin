from typing import Optional, List

from pydantic import BaseModel, EmailStr, constr


# Shared properties
class UserBase(BaseModel):
  username: Optional[str] = None
  fullname: Optional[str] = None
  email: Optional[EmailStr] = None
  is_active: Optional[bool] = True
  is_superuser: bool = False
  roles: Optional[List[int]] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
  username: constr(min_length=4, max_length=12, regex="^[a-zA-Z0-9_-]+$")  # noqa: F722
  password: constr(min_length=8, max_length=30)


# Properties to receive via API on update
class UserUpdate(UserBase):
  ...


class User(UserBase):
  id: Optional[int] = None

  class Config:
    # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
    #  but an ORM model (or any other arbitrary object with attributes).
    orm_mode = True


class UserMe(User):
  permissions: Optional[List[str]] = None


class UserList(BaseModel):
  total: int
  items: List[User]
