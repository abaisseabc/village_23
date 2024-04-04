from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CallRequestsSerializer


# Create your views here.

class CallRequestCreateAPIView(APIView):
    """Создание заявки на звонок"""

    def post(self, request, *args, **kwargs):
        serializer = CallRequestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
