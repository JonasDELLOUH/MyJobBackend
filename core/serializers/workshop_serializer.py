from rest_framework import serializers

from core.models.adress import Address
from core.models.workshop import Workshop
from core.serializers.adress_serializer import AddressSerializer


class WorkshopSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False, read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(write_only=True, source='address', queryset=Address.objects.all())

    class Meta:
        model = Workshop
        fields = [
            'workshopName',
            'workshopImageUrl',
            'address',
            'address_id'
        ]
