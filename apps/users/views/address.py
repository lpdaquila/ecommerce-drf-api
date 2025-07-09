from apps.users.models import Address, Profile
from apps.users.serializers import AddressSerializer
from apps.users.views.base import Base
from apps.users.schemas.address import AddressSchema
from apps.utils.data_parser import validation_error_detail_msg

from pydantic import ValidationError 

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class AddressView(Base):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = self.get_profile(request.user.id)
        
        addresses = Address.objects.filter(profile_id=profile.pk).all() # type: ignore
        
        serializer = AddressSerializer(addresses)
        
        return Response({
            "addresses": serializer.data
        })
    
    def post(self, request):
        try:
            validated_data = AddressSchema(**request.data)
        except ValidationError as e:
            detail = validation_error_detail_msg(e.errors())
            raise APIException(detail=detail)
        
        profile = self.get_profile(request.user.id)
        
        created_addr = Address.objects.create(
            profile_id=profile.pk,
            address_name=validated_data.address_name,
            address=validated_data.address,
            number=validated_data.number,
            complement=validated_data.complement,
            district=validated_data.district,
            zip_code=validated_data.zip_code,
            city=validated_data.city,
            state=validated_data.state
        )
        
        if isinstance(created_addr, Address):
            return Response({"success": True}, status=201)
        
        return Response(created_addr, status=400)
    
class AddressDetailView(Base):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, address_id):
        profile = self.get_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.id, address_id=address_id) # type: ignore
        
        serializer = AddressSerializer(address)
        
        return Response({"address": serializer.data})
    
    def put(self, request, address_id):
        try:
            validated_data = AddressSchema(**request.data)
        except ValidationError as e:
            detail = validation_error_detail_msg(e.errors())
            raise APIException(detail=detail)
        
        profile = self.get_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.pk, address_id=address_id)
        
        Address.objects.filter(id=address.pk).update(
            address_name=validated_data.address_name,
            address=validated_data.address,
            number=validated_data.number,
            complement=validated_data.complement,
            district=validated_data.district,
            zip_code=validated_data.zip_code,
            city=validated_data.city,
            state=validated_data.state
        )
        
        return Response({"success": True})
    
    def delete(self, request, address_id):
        profile = self.get_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.pk, address_id=address_id)
        
        address.delete()
        
        return Response({"success": True})
    
    