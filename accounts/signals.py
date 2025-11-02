from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth import user_logged_in
from django.contrib.auth.views import PasswordResetConfirmView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.signals import password_reset

from django.contrib.auth.signals import user_logged_in


