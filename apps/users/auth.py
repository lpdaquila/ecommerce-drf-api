# type: ignore
from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from apps.users.models import User

class Authentication:
    def login(self, email:str=None, password:str=None) -> User:
        exception_auth = AuthenticationFailed('Incorrect email or password.')
        
        user_exists = User.objects.filter(email=email).exists()
        
        if not user_exists:
            raise exception_auth
        
        user = User.objects.filter(email=email).first()
        
        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(
        self,
        name: str,
        email: str,
        password: str,
        staff=False
    ) -> User:
        
        if not name or name == '':
            raise APIException('Name cannot be null')
        
        if not email or email == '':
            raise APIException('Email cannot be empty')
        
        if not password or password == '':
            raise APIException('Password cannot be empty')
        
        user = User 
        if user.objects.filter(email=email).exists():
            raise APIException('Email already in use!')
        
        password_hashed = make_password(password)
        
        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            staff=False
        )
        
        return created_user