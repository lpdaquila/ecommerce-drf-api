from rest_framework import serializers

from apps.users.models import Profile
        
class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('id', 'name')
        
    def get_name(self, obj):
        return obj.user.name if obj.user else obj.guest_name
    
class ProfileDetailSerializer(serializers.ModelSerializer):
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
        return obj.document if obj.document else None
    
    def get_phone(self, obj):
        return obj.phone if obj.phone else None
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        