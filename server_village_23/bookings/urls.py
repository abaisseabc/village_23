from django.urls import path

from .views import BookingCreateAPIView

urlpatterns = [
    path('bookings/', BookingCreateAPIView.as_view()),
]
