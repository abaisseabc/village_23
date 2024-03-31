from django.urls import path

from .views import AllNews, LatestNews

urlpatterns = [
    path("all_news/", AllNews.as_view()),
    path("latest_news/", LatestNews.as_view()),
]
