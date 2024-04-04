from rest_framework import serializers

from .models import CallRequests


class CallRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRequests
        fields = ["call_id", "phone_number", "date_added"]
