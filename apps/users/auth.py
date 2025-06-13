from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from apps.users.models import User

def get_user(method: str, email:str, password:str="") -> User | None: 
    """
    Function that receives a method related to the use 
    (signup or login), executes the SQL query, and based in the use,
    returns a 'User' object from the data models or 'None'.
    
    If method is 'login' and the query returns 'None' will throw the 'exception_auth'
    because the user was not found.
    
    If method is 'signup' and the query returns the first result will throw the
    APIException 'Email already in use' 
    
    Args:
        :method (str): ["login" | "signup"] method that will be used to change the flow of data to be returned
        :email (str): User email to be consulted.
        :password (str) [Optional]: User password to authenticate the user (optional for 'signup' method).
    
    Returns:
        :User (class models): Returns an object of type 'User' from the
        models class if login has been successfull |
        :None: If the method is 'signup' and the query returns 'None'.
    """
    exception_auth = AuthenticationFailed('Incorrect email or password.')
        
    query = """
        SELECT * FROM "users_user" 
        WHERE "users_user"."email" = %s"""
    try:
        user = User.objects.raw(query, [email])[0] # First result
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
    """
    Class for user authentication
    
    This class performs the login and signup methods.
    """
    def login(self, email:str, password:str) -> User | None: 
        """
        Logs the user in based on the provided email and password, and returns
        a 'User' object with the data returned from the 'get_user()' function.
        
        Args:
            :email (str): The given user email
            :password (str): The given user password
            
        Returns:
            :User (class models): Returns an object of type 'User' from the
            models class
        """
        
        user = get_user('login', email, password)
        
        return user 
    
    def signup(
        self,
        name: str,
        email: str,
        password: str,
        staff=False
    ) -> User:
        """
        Registers the user based on the provided data, 
        as long as the user provides an email different 
        from one that may already be registered.
        
        Args:
            :name (str): [Not Null] The user name
            :email (str): [Not Null] The user email (cannot already be registred)
            :password (str): [Not Null] The user password
            :staff (bool): [Optional] For future use
            
        Returns:
            :User (class models): Returns an object of type 'User' from models class
        """
        
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