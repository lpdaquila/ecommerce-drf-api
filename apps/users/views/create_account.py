from apps.users.views.base import Base
from apps.users.services import Authentication
from apps.users.serializers import UserProfileSerializer
from apps.users.schemas.user import UserSignupSchema

from rest_framework.response import Response

class CreateAccountView(Base):
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
        data = UserSignupSchema(**request.data)
        
        user = Authentication.create_account(self, name=data.name, email=data.email, password=data.password) # type: ignore
        
        profile = self.get_user_profile(user_id=user.pk)
        
        serializer = UserProfileSerializer(profile)
        
        return Response({
            "user": serializer.data,
        })
