from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NewsSerializers
from .models import News


# Create your views here.

class AllNews(APIView):
    """Получение всех новостей"""

    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializers(news, many=True)
        return Response(serializer.data)


class LatestNews(APIView):
    """Получение последних двух новостей"""

    def get(self, request, format=None):
        news = News.objects.all()[0:2]
        serializer = NewsSerializers(news, many=True)
        return Response(serializer.data)
