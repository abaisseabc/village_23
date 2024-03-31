from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Rooms
from .serializers import RoomsSerializers


# Create your views here.

class RoomsForClient(APIView):
    """Получение комнат для отображения на клиенте"""

    def get(self, request, format=None):
        rooms = Rooms.objects.all()[0:2]
        serializer = RoomsSerializers(rooms, many=True)
        return Response(serializer.data)
