import re
from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Optional
from apps.utils.exceptions import InvalidZipCodeFormat

class AddressSchema(BaseModel):
    address_name: Annotated[str, Field(max_length=100)]
    address: Annotated[str, Field(max_length=255)]
    number: Annotated[str, Field(max_length=10)]
    complement: Optional[Annotated[str, Field(max_length=255)]] = None
    district: Annotated[str, Field(max_length=100)]
    zip_code: Annotated[str, Field(max_length=10)]
    city: Annotated[str, Field(max_length=100)]
    state: Annotated[str, Field(max_length=2)]
    
    @field_validator('zip_code')
    def validate_zip_code(cls, v):
        if not re.match(r"^\d{5}-\d{3}$", v):
            raise InvalidZipCodeFormat
        return v