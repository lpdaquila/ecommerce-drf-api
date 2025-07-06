from apps.users.views.base import Base
from apps.users.models import User
from apps.users.serializers import ProfileSerializer
from apps.utils import load_query

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class GetUserView(Base):
    """
    Class for check if the user is authenticated
    """
    permission_classes=[IsAuthenticated]
    
    def get(self, request) -> None:
        """
        Endpoint Method 'GET' that checks if the user is authenticated.
        
        It recieves a request and checks if user exists or is activated in database
        
        Gets the user permissions from the method 'get_user_access' giving the User instance
        
        Args:
            :request (HTTP Request): Recieves a HTTP Request with user data.
        
        Returns:
            :Response (rest_framework Response): A JSON serialized with value/key 
            ("user": serializer.data, "perm": List[str])
            containing the user data and a list of permissions
        """
        query = load_query.load('apps/users/sql/get_user.sql')
        try:
            user = User.objects.raw(query, [request.user.id])[0]
        except IndexError:
            APIException('User does not exists or is inactivated!')
            return
        
        profile = self.get_user_profile(user.pk)
            
        serializer = ProfileSerializer(profile)
        
        return Response({
            "profile": serializer.data
        })  # type: ignore
            