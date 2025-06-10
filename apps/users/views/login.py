from apps.users.views.base import Base

class Login(Base):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        

class Logout(Base):
    pass