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
    """Получение последних трех новостей"""

    def get(self, request, format=None):
        news = News.objects.all()[0:3]
        serializer = NewsSerializers(news, many=True)
        return Response(serializer.data)


class NewDetail(APIView):
    def get(self, request, new_slug, format=None):
        new = News.objects.get(slug=new_slug)
        serializer = NewsSerializers(new)
        return Response(serializer.data)
