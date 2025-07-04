from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from apps.users.models import User

def get_user(email:str) -> User | None: 
    """
    Function that executes the SQL query, and
    returns a 'User' object from the data models or 'None'.
    
    Args:
        :email (str): User email to be consulted.
    
    Returns:
        :User (class models): Returns an object of type 'User' from the
    """
        
    query = """
        SELECT * FROM "users_user" 
        WHERE "users_user"."email" = %s
        LIMIT 1"""
        
    user = next(iter(User.objects.raw(query, [email])), None)
    
    return user 

def create_user(name: str, email: str, password: str) -> User:
    password_hashed = make_password(password)
    
    created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            staff=False
        )
    
    return created_user

class Authentication:
    """
    Class for user authentication
    
    This class performs the login and signup methods.
    """
    
    def login(self, email:str, password:str) -> User | None: 
        """
        Logs the user in based on the provided email and password, and returns
        a 'User' object with the data returned from the 'get_user()' function.
        
        Args:
            :email (str): User email
            :password (str): User password
            
        Returns:
            :User (class models): Returns an object of type 'User' from the
            models class
        """
        
        user = get_user(email)
        
        if not user or not check_password(password, user.password):
            raise AuthenticationFailed('Incorrect email or password.')
        
        return user 
    
    def signup(
        self,
        name: str,
        email: str,
        password: str,
    ) -> User:
        """
        Registers the user based on the provided data, 
        as long as the user provides an email different 
        from one that may already be registered.
        
        Args:
            :name (str): [Not Null] The user name
            :email (str): [Not Null] The user email (cannot already be registred)
            :password (str): [Not Null] The user password
            
        Returns:
            :User (class models): Returns an object of type 'User' from models class
        """
        
        if not name or name == '':
            raise APIException('Name cannot be null')
        
        if not email or email == '':
            raise APIException('Email cannot be empty')
        
        if not password or password == '':
            raise APIException('Password cannot be empty')

        if get_user(email): # Checks if the email already exists
            raise APIException('Email already exists')
        
        return create_user(name, email, password)