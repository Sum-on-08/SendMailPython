from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class SendEmailView(APIView):
    def post(self, request):
        # Extract email data from the request
        subject = request.data.get("subject", "Default Subject")
        message = request.data.get("message", "This is a test email from Django API.")
        recipient_email = request.data.get("recipient_email")

        if not recipient_email:
            return Response({"error": "Recipient email is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Sender email
                [recipient_email],  # Recipient email in a list
                fail_silently=False,
            )
            return Response({"message": "✅ Email sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestEndpoint(APIView):
    def get(self, request):
        return Response({"message": "Hello, World! from django"}, status=status.HTTP_200_OK)
