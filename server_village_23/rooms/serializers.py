from rest_framework import serializers

from .models import TypeRooms, Rooms


class TypeRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRooms
        fields = (
            "type",
            "type_rus",
            "description"
        )


class RoomsSerializers(serializers.ModelSerializer):
    room_type = TypeRoomsSerializer()

    class Meta:
        model = Rooms
        fields = (
            "room_type",
            "view_window",
            "size",
            "type_bed",
            "price",
            "get_image"
        )
