from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from apps.users.models import User
from apps.utils import load_query

def get_user(method: str, email:str, password:str=None) -> User | None: # type: ignore
    exception_auth = AuthenticationFailed('Incorrect email or password.')
        
    query = load_query.load('apps/users/sql/login_user.sql')
    try:
        user_exists = User.objects.raw(query, [email]) 
        user = user_exists[0]
        if method == "signup":
            raise APIException('Email already in use!')
        if not check_password(password, user.password):
            raise exception_auth    
            
        return user
                
    except IndexError:
        if method == "login":
            raise exception_auth
        else:
            pass

class Authentication:
    def login(self, email:str=None, password:str=None) -> User | None: # type: ignore
        
        user = get_user('login', email, password)
        
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

        get_user('signup', email)
        
        password_hashed = make_password(password)
        
        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            staff=False
        )
        
        return created_user