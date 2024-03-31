from rest_framework import serializers

from .models import News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "slug",
            "description",
            "date_added",
            "get_image"
        )
