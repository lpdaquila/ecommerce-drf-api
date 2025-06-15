from apps.users.views.base import Base
from apps.users.auth import Authentication
from apps.users.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Login(Base):
    """Logs the user in"""
    def post(self, request):
        """
        Endpoint Method 'POST' that recieves a resquest with user data
        
        Logs the user in with Authentication.login() method 
        
        Serialize the user
        
        Generates a refresh JWT token for user session
        
        Args:
            :request (HTTP Request): 
                email (str): User email
                password (str): User password 
                
        Returns:
            :Response (rest_framework Response): Returns a dict with user serialized data, user permissions, refresh token and access token
                
        """
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Authentication.login(self, email=email, password=password) # type: ignore
        
        token = RefreshToken.for_user(user) # type: ignore
        
        access = self.get_user_access(user.pk)  # type: ignore
        
        serializer = UserSerializer(user)
        
        return Response({
            "user": serializer.data,
            "user_access": access,
            "refresh": str(token),
            "access": str(token.access_token),
        })

class Logout(Base):
    pass