from apps.users.views.base import Base
from apps.users.auth import Authentication
from apps.users.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class Login(Base):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Authentication.login(self, email=email, password=password) # type: ignore
        
        token = RefreshToken.for_user(user) # type: ignore
        
        access = self.get_user_access(user.id) # type: ignore
        
        serializer = UserSerializer(user)
        
        return Response({
            "user": serializer.data,
            "user_access": access,
            "refresh": str(token),
            "access": str(token.access_token),
        })

class Logout(Base):
    pass