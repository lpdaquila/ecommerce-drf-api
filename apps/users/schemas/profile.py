from apps.utils.data_parser import phone_to_number, document_to_number, validate_cpf
from apps.utils.exceptions import InvalidPhone, InvalidDocument

from pydantic import BaseModel, EmailStr, UUID4, Field, field_validator
from typing import Optional, Annotated
from datetime import datetime

class ProfileSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=100)]
    email: EmailStr
    phone: Optional[str] = None
    document: Optional[str] = None 
    
    @field_validator('phone')
    def validate_phone_format(cls, v):
        if v:
            numeric = phone_to_number(v)
            if len(numeric) < 10 or len(numeric) > 15:
                raise InvalidPhone
            return numeric
        else:
            return None
    
    @field_validator('document')
    def validate_document_format(cls, v):
        if v:
            parsed = document_to_number(v)
            if len(parsed) < 11 or len(parsed) > 15 or not validate_cpf(parsed):
                raise InvalidDocument
            return parsed
        else:
            return None
    
    class Config:
        orm_mode = True
        
class AnonProfileSchema(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=100)]
    email: EmailStr
    public_id: UUID4
    expires_at: datetime