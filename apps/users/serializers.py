from rest_framework import serializers

from apps.users.models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')
        
class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    document = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'phone', 'document')
        
    def get_name(self, obj):
        return obj.user.name if obj.user else obj.guest_name
    
    def get_email(self, obj):
        return obj.user.email if obj.user else obj.guest_email
        
    def get_phone(self, obj):
        return obj.phone if obj.phone else None
    
    def get_document(self, obj):
        return obj.document if obj.document else None
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        