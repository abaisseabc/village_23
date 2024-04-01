from django.urls import path

from .views import AllNews, LatestNews, NewDetail

urlpatterns = [
    path("all_news/", AllNews.as_view()),
    path("latest_news/", LatestNews.as_view()),
    path("news/<slug:new_slug>", NewDetail.as_view()),
]
