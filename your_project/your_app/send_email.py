import os
import django

# Set up Django environment (if running this script standalone)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Replace 'your_project' with your actual project name
django.setup()

from django.core.mail import send_mail

def test_email():
    subject = "Test Email from Django"
    message = "Hello! This is a test email sent using Django."
    from_email = "settings.EMAIL_HOST_USER"  # Replace with your Gmail
    recipient_list = ["recipient@example.com"]  # Replace with the recipient email

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    test_email()
