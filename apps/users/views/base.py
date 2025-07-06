from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from apps.utils.exceptions import NotFoundProfile
from apps.users.models import Profile
from apps.users.models.users import GroupPermissions, User, UserGroups
from apps.users.selectors import get_user

class Base(APIView):
    """
    Base class for the views extending the "APIView" class
    """
    def get_user(self, email:str) -> User | None: 
        return get_user(email=email)
    
    def get_user_profile(self, user_id):
        profile = Profile.objects.filter(user_id=user_id).first()
        
        if not profile:
            raise NotFoundProfile
        
        return profile
    
    def get_profile(self, profile_id):
        profile = Profile.objects.filter(profile_id=profile_id).first()
        
        if not profile:
            raise NotFoundProfile
        
        return profile
        
        