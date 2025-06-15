from apps.users.views.base import Base
from apps.users.auth import Authentication
from apps.users.serializers import UserSerializer

from rest_framework.response import Response

class SignUp(Base):
    """Register a new user"""
    def post(self, request):
        """
        Endpoint Method 'POST' that recieves a request with user data
        
        Create a new user with Authentication.signup() method
        
        Serialize the new user 
        
        Returns the user serialized data
        
        Args:
            :request (HTTP Request):
                name (str): User name
                email (str): User email (cannot be already registered)
                password (str): User password
                
        Returns:
            :Response (rest_framework Response): Returns a dict with user serialized data.
        """
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Authentication.signup(self, name=name, email=email, password=password)  # type: ignore
        
        serializer = UserSerializer(user)
        
        return Response({
            "user": serializer.data,
        })
