from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializers the 'User" model for the API requests data.
    """
    class Meta:
        """
        Recieves the 'User' model and serialize to "fields"
        
        Serialized data:
            :id: User Primary Key
            :name: User name
            :email: User email
        """
        model = User
        fields = ('id', 'name', 'email')
        
class ProfileSerializer(serializers.ModelSerializer):
    ...
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        