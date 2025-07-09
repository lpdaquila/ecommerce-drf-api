from apps.users.views.base import Base
from apps.users.services import Authentication
from apps.users.serializers import UserProfileSerializer
from apps.users.schemas.user import UserAuthSchema
from apps.utils.data_parser import validation_error_detail_msg

from pydantic import ValidationError

from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(Base):
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
        try:
            data = UserAuthSchema(**request.data)
        except ValidationError as e:
            detail = validation_error_detail_msg(e.errors())
            raise APIException(detail=detail)
        
        user = Authentication.login(self, email=data.email, password=data.password)  # type: ignore
        
        token = RefreshToken.for_user(user)  # type: ignore
        
        profile = self.get_user_profile(user_id=user.pk) # type: ignore
        
        serializer = UserProfileSerializer(profile)
        
        return Response({
            "user": serializer.data,
            "refresh": str(token),
            "access": str(token.access_token),
        })