from django.urls import path

from .views import EventRetrieveAPIView

urlpatterns = [
    # path("", EventListApiView.as_view()),
    path("event/<int:pk>/", EventRetrieveAPIView.as_view()),
]
