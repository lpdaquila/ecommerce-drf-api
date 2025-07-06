from rest_framework import serializers

from apps.users.models import Profile
        
class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ('id', 'name')
        
    def get_name(self, obj):
        return obj.user.name if obj.user else obj.guest_name
    
class AddressSerializer(serializers.ModelSerializer):
    ...
        
        