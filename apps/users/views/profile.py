from apps.utils.exceptions import RequiredFields
from apps.users.serializers import ProfileSerializer
from apps.users.views.base import Base
from apps.users.models import Profile

from rest_framework.views import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import APIException

class GuestProfile(Base):
    permission_classes = [AllowAny]
    
    """
    For checkout logic: 
    
    put on the api headers the "X-Gst-Token" and in frontend store in localStorage or in a cookie
    for the uuid token to guest user
    
    in checkout view use "HasValidGuestToken" in permission_classes
    """
    
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        document = request.data.get('document')
        
        if not name or email:
            raise RequiredFields
        
        if Profile.objects.filter(email=email).exists():
            raise APIException('Email already in use!')
        
        new_guest_profile = Profile.objects.create(
            name=name,
            email=email,
            phone=phone,
            document=document
        )
        
        if isinstance(new_guest_profile, Profile):
            return Response({"success": True}, status=201)
        
        return Response(new_guest_profile, status=400)
    
class UserProfile(Base):
    ...
    
    