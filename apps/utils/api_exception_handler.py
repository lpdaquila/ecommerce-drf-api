from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from pydantic import ValidationError

def api_exception_handler(exc, context):
    
    if isinstance(exc, ValidationError):
        print('chegou aqui')
        error = exc.errors()[0]['msg']
        return exception_handler(APIException(detail=error), context)
    print('nao eh erro')
    
    return exception_handler(exc, context)