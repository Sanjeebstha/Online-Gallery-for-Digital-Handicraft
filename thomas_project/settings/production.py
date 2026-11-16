from .base import *

DEBUG = False
ALLOWED_HOSTS = ['thomas-hachtmann.de', 'www.thomas-hachtmann.de' ,'localhost', '127.0.0.1',]#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# CSRF Fix for Nginx proxy 
CSRF_TRUSTED_ORIGINS = ['https://thomas-hachtmann.de', 'https://www.thomas-hachtmann.de',]

# Enforce HTTPS
SECURE_SSL_REDIRECT = True # True only when you have HTTPS
SESSION_COOKIE_SECURE = True # True only when you have HTTPS
CSRF_COOKIE_SECURE = True # True only when you have https
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Session expires after 30 min
SESSION_COOKIE_AGE = 1800
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
