import re
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated
from apps.utils.exceptions import InvalidPasswordFormat

class UserSignupSchema(BaseModel):
    name: Annotated[str, Field(max_length=100)]
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]
    
class UserAuthSchema(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]
    
    # @field_validator('password')
    # def validate_password(cls, v):
    #     if not re.match(r"^.{8,}$", v):
    #         raise InvalidPasswordFormat
    #     return v
    