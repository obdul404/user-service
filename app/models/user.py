from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    firstname: str
    lastname: str
    email: str
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
