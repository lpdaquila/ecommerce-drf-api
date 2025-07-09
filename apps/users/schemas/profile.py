import re

from apps.utils.data_parser import phone_to_number, document_to_number, validate_cpf
from apps.utils.exceptions import InvalidPhone, InvalidDocument

from pydantic import BaseModel, EmailStr, UUID4, Field, field_validator
from typing import Optional, Annotated
from datetime import datetime

class ProfileSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=100)]
    email: EmailStr
    phone: Optional[Annotated[str, Field(min_length=10, max_length=15)]] = None
    document: Optional[Annotated[str, Field(min_length=11, max_length=14)]] = None 
    
    @field_validator('phone')
    def validate_phone_format(cls, v):
        numeric = phone_to_number(v)
        if len(numeric) < 10 or len(numeric) > 15:
            raise InvalidPhone
        return numeric
    
    @field_validator('document')
    def validate_document_format(cls, v):
        parsed = document_to_number(v)
        if len(parsed) < 11 or len(parsed) > 15 or not validate_cpf(parsed):
            raise InvalidDocument
        return parsed
    
    class Config:
        orm_mode = True
        
class AnonProfileSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=100)]
    email: EmailStr
    public_id: UUID4
    expires_at: datetime