from rest_framework.exceptions import APIException

class RequiredFields(APIException):
    status_code = 400
    default_detail = 'Required fields are missing'
    default_code = 'error_required_field'
    
class EmailAlreadyInUse(APIException):
    status_code = 400
    default_detail = 'Email already in use'
    default_code = 'error_email_already_in_use'
    
class NotFoundProfile(APIException):
    status_code = 404
    default_detail = 'Profile not found'
    default_code = 'profile_not_found'
    
class UserInactivated(APIException):
    status_code = 401
    default_detail = "User is inactivated"
    default_code = 'error_user_inactivated'
    
class DocumentAlreadyRegistered(APIException):
    status_code = 400
    default_detail = "Document already registered"
    default_code = 'error_document_already_registered'
    
class InvalidPhone(APIException):
    status_code = 400
    default_detail = "Invalid phone format"
    
class InvalidDocument(APIException):
    status_code = 400
    default_detail = "Invalid document format"
    
class InvalidPasswordFormat(APIException):
    status_code = 400
    default_detail = "Invalid password format"
    
class InvalidZipCodeFormat(APIException):
    status_code = 400
    default_detail = "Invalid zip code format, Use XXXXX-XXX pattern"
    
    