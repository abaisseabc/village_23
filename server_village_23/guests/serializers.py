from rest_framework import serializers

from .models import GuestServices


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestServices
        fields = ["guest_id_service", "service_name"]
