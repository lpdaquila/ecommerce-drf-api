from rest_framework import serializers

from apps.users.models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    """
    Serializers the 'User" model for the API requests data.
    """
    phone = serializers.SerializerMethodField()
    
    class Meta:
        """
        Recieves the 'User' model and serialize to "fields"
        
        Serialized data:
            :id: User Primary Key
            :name: User name
            :email: User email
        """
        model = User
        fields = ('id', 'name', 'email', 'phone', 'document')
        
    def get_phone(self, obj):
        return obj.phone if obj.phone else None
        
class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    document = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'phone', 'document')
        
    def get_phone(self, obj):
        return obj.phone if obj.phone else None
    
    def get_document(self, obj):
        return obj.document if obj.document else None
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        