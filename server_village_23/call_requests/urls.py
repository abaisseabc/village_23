from django.urls import path

from .views import CallRequestCreateAPIView

urlpatterns = [
    path("call_requests/", CallRequestCreateAPIView.as_view()),
]
