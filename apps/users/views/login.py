from apps.users.views.base import Base
from apps.users.services import Authentication
from apps.users.serializers import UserSerializer, ProfileSerializer

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
        
        profile = self.get_user_profile(user_id=user.pk) # type: ignore
        
        user_serializer = UserSerializer(user)
        
        profile_serializer = ProfileSerializer(profile)
        
        return Response({
            "user": user_serializer.data,
            "profile": profile_serializer.data,
            "refresh": str(token),
            "access": str(token.access_token),
        })