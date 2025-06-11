from apps.users.views.base import Base
from apps.users.auth import Authentication
from apps.users.serializers import UserSerializer

from rest_framework.response import Response

class SignUp(Base):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Authentication.signup(self, name=name, email=email, password=password) # type: ignore
        
        serializer = UserSerializer(user)
        
        return Response({
            "user": serializer.data,
        })
