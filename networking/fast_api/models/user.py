from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class UserRole(str, Enum):
    admin = "Admin"
    guest = "Guest"


class User(BaseModel):
    username: str
    password: str
    role: Optional[UserRole] = Field(UserRole.guest, description="User role (admin, or guest)")
