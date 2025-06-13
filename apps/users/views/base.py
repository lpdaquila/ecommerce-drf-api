from typing import Any
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from apps.users.models.user import GroupPermissions, User, UserGroups

class Base(APIView):
    """
    Base class for the views extending the "APIView" class
    """
    def get_user_access(self, user_id: int) -> dict[str, Any] | None:
        """
        Method that queries a user's permissions and returns them in a list of dicts.
        
        Args:
            :user_id (int): The PK of the User
            
        Returns:
            :dict[str, Any]: Returrns a list of dicts containing the permission "id", "label" and "codename"
            from the GroupPermissions model.
        """
        access = {
            "permissions": []
        }
        
        # permissions['staff'] = User.objects.filter(user_id=user_id).get('staff')
        
        groups = UserGroups.objects.filter(user_id=user_id).all()
        
        for g in groups:
            group = g.group
            permissions = GroupPermissions.objects.filter(group_id=group.id).all() # type: ignore
            
            for p in permissions:
                access['permissions'].append({
                    "id": p.permission.id, # type: ignore
                    "label": p.permission.name,
                    "codename": p.permission.codename,
                })
        
        return access
        
        