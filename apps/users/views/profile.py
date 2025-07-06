from apps.utils.exceptions import RequiredFields
from apps.users.serializers import ProfileDetailSerializer
from apps.users.views.base import Base
from apps.users.models import Profile, User
from apps.utils.exceptions import EmailAlreadyInUse, UserInactivated

from rest_framework.views import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import APIException

class GuestProfileView(Base):
    permission_classes = [AllowAny]
    
    """
    For checkout logic: 
    
    put on the api headers the "X-Gst-Token" and in frontend store in localStorage or in a cookie
    for the uuid token to guest user
    
    in checkout view use "HasValidGuestToken" in permission_classes
    """
    
    #### CREATE GUEST PROFILE ####
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
    
class ProfileDetailView(Base):
    permission_classes=[IsAuthenticated]
    
    def get(self, _request, profile_id):
        profile = Profile.objects.filter(profile_id=profile_id).first()
        
        is_active = profile.user.is_active # type: ignore
        
        if not is_active:
            raise UserInactivated
        
        serializer = ProfileDetailSerializer(profile)
        
        return Response({
            "profile": serializer.data
        })
        
    def put(self, request, profile_id):
        name = request.data.get('name')
        email = request.data.get('email')
        document = request.data.get('document')
        phone = request.data.get('phone')
        
        profile = self.get_profile(profile_id)
        
        if email != profile.user.email and User.objects.filter(email=email).exists(): # type: ignore
            raise EmailAlreadyInUse
        
        User.objects.filter(id=profile.user.pk).update(  # type: ignore
            name=name,
            email=email,
        )
        
        Profile.objects.filter(id=profile.pk).update(
            document=document,
            phone=phone
        )
        
        return Response({"success": True})
    
    def delete(self, _request, profile_id):
        profile = self.get_profile(profile_id)
        
        profile.delete()
        
        return({"success": True})
    
    