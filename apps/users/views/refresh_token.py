from apps.users.views.base import Base

from rest_framework.views import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class TokenRefreshView(Base):
    def post(self, request):
        refresh_token = request.data.get("refresh")
        
        if not refresh_token:
            return Response({"detail": "No refresh token given"})
        
        try:
            refresh = RefreshToken(refresh_token)
            
            access_token = refresh.access_token
            
            return Response({
                "access": str(access_token),
            }, status=200)
            
        except TokenError as e:
            return Response({"detail": str(e)}, status=401)