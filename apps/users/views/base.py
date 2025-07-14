from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.utils.exceptions import NotFoundProfile
from apps.users.models import Profile, Address, User

class Base(APIView):
    """
    Base class for the views extending the "APIView" class
    """
    
    def get_user(self, user_id):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            return Response({"detail": "User not found"}, status=404)
        
        return user
    
    def get_user_profile(self, user_id):
        profile = Profile.objects.filter(user_id=user_id).first()
        
        if not profile:
            raise NotFoundProfile
        
        return profile
    
    def get_profile(self, profile_id):
        profile = Profile.objects.filter(id=profile_id).first()
        
        if not profile:
            raise NotFoundProfile
        
        return profile
    
    def get_user_address(self, profile_id, address_id):
        address = get_object_or_404(Address, pk=address_id, profile_id=profile_id)
        
        return address
        
        