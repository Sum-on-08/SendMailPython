from django.urls import path
from .views import SendEmailView, TestEndpoint

urlpatterns = [
    path("send-email/", SendEmailView.as_view(), name="send-email"),
    path("test/",TestEndpoint.as_view(), name="test-endpoint"),
]
