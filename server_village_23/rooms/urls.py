from django.urls import path

from .views import RoomsForClient

urlpatterns = [
    path("rooms/", RoomsForClient.as_view()),
]
