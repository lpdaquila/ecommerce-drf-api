from rest_framework import serializers

from apps.users.models import Profile
from apps.utils.data_parser import document_to_string, phone_to_string
        
class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('id', 'name')
        
    def get_name(self, obj):
        return obj.user.name 
    
class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    document = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = (
            'id',
            'name',
            'email',
            'document',
            'phone',
        )
        
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_document(self, obj):
        return document_to_string(obj.document) if obj.document else None
    
    def get_phone(self, obj):
        return phone_to_string(obj.phone) if obj.phone else None
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        