from rest_framework.exceptions import APIException

class RequiredFields(APIException):
    status_code = 400
    default_detail = 'Required fields are missing'
    default_code = 'error_required_field'
    
class NotFoundProfile(APIException):
    status_code = 404
    default_detail = 'Profile not found'
    default_code = 'profile_not_found'