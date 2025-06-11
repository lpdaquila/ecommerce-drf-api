from typing import Any
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from apps.users.models.user import GroupPermissions, User, UserGroups

class Base(APIView):
    def get_user_access(self, user_id) -> dict[str, Any] | None:
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
        
        