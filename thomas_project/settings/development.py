from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ✅ Allows 2FA login without HTTPS in dev
TWO_FACTOR_CALL_GATEWAY = None
TWO_FACTOR_SMS_GATEWAY = None

# Relaxed HTTPS requirements for local dev
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
