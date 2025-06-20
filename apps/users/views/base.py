from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from apps.utils.exceptions import NotFoundProfile
from apps.users.models import Profile
from apps.users.models.users import GroupPermissions, User, UserGroups

class Base(APIView):
    """
    Base class for the views extending the "APIView" class
    """
    def get_user(self, user_id: int):...
    
    def get_profile(self, profile_id):
        profile = Profile.objects.filter(profile_id=profile_id).first()
        
        if not profile:
            raise NotFoundProfile
        
        return profile
        
        