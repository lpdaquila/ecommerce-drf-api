from apps.users.models.users import User


def get_user(email:str) -> User | None: 
    """
    Function that executes the SQL query, and
    returns a 'User' object from the data models or 'None'.
    
    Args:
        :email (str): User email to be consulted.
    
    Returns:
        :User (class models): Returns an object of type 'User' from the
    """
        
    user = User.objects.filter(email=email).first()
    
    return user 