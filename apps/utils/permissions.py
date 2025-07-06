from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.users.models.profile import Profile

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
class HasValidGuestToken(BasePermission):
    def has_permission(self, request, view):  # type: ignore
        token = request.headers.get("X-Gst-Token")
        if not token:
            return False
        
        try:
            profile = Profile.objects.get(guest_public_id=token)
        except Profile.DoesNotExist:
            return False
        
        if not profile.is_valid_token():
            return False
        
        request.profile = profile
        return True
    
class IsAuthenticatedOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated