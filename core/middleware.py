from typing import Any
from django.http import JsonResponse

class JsonExceptionMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request) -> Any:
        try:
            return self.get_response(request)
        except Exception as e:
            return JsonResponse({
                "detail": f"Internal server error: {e}"
            }, status=500)