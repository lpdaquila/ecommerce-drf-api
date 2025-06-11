from apps.users.views.base import Base
from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.utils import load_query

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class GetUser(Base):
    permission_classes=[IsAuthenticated]
    
    def get(self, request) -> None:
        query = load_query.load('apps/users/sql/get_user.sql')
        try:
            user = User.objects.raw(query, [request.user.id])[0]
        except IndexError:
            APIException('User does not exists or is inactivated!')
            
        access = self.get_user_access(user) # type: ignore
            
        serializer = UserSerializer(user) # type: ignore
        
        return Response({
            "user": serializer.data,
            "perm": access,
        }) # type: ignore
            