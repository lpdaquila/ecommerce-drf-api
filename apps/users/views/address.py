from apps.users.models import Address, Profile
from apps.users.serializers import AddressSerializer
from apps.users.views.base import Base

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
        address_name = request.data.get('address_name')
        address = request.data.get('address')
        number = request.data.get('number')
        complement = request.data.get('complement')
        district = request.data.get('district')
        zip_code = request.data.get('zip_code')
        city = request.data.get('city')
        state = request.data.get('state')
        
        profile = self.get_profile(request.user.id)
        
        created_addr = Address.objects.create(
            profile_id=profile.pk,
            address_name=address_name,
            address=address,
            number=number,
            complement=complement,
            district=district,
            zip_code=zip_code,
            city=city,
            state=state
        )
        
        if isinstance(created_addr, Address):
            return Response({"success": True}, status=201)
        
        return Response(created_addr, status=400)
    
class AddressDetailView(Base):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, address_id):
        profile = self.get_user_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.id, address_id=address_id) # type: ignore
        
        serializer = AddressSerializer(address)
        
        return Response({"address": serializer.data})
    
    def put(self, request, address_id):
        address_name = request.data.get('address_name')
        address = request.data.get('address')
        number = request.data.get('number')
        complement = request.data.get('complement')
        district = request.data.get('district')
        zip_code = request.data.get('zip_code')
        city = request.data.get('city')
        state = request.data.get('state')
        
        profile = self.get_user_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.pk, address_id=address_id)
        
        Address.objects.filter(id=address.pk).update(
            address_name=address_name,
            address=address,
            number=number,
            complement=complement,
            district=district,
            zip_code=zip_code,
            city=city,
            state=state
        )
        
        return Response({"success": True})
    
    def delete(self, request, address_id):
        profile = self.get_user_profile(request.user.id)
        
        address = self.get_user_address(profile_id=profile.pk, address_id=address_id)
        
        address.delete()
        
        return Response({"success": True})
    
    