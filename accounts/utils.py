import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return "%06d" % random.randint(0, 999999)

def send_otp_email(user, otp):
    subject = "Your E-Com verification OTP"
    message = f"Hello {user.username},\n\nYour OTP is: {otp}\n\nThanks,\nE-Com Team"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
