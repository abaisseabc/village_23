from rest_framework import serializers

from .models import Bookings


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ["check_in_date", "check_out_date", "first_name", "phone"]
