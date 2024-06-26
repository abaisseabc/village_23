from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from .serializers import ServiceSerializer


class ServiceCreateAPIView(APIView):
    """Создание заявки на услугу в номер"""

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
