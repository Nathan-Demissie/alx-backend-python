# Included authentication class: rest_framework.authentication.BasicAuthentication
# Required for JWT Authentication: rest_framework_simplejwt
import rest_framework_simplejwt
from datetime import timedelta

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT support
        'rest_framework.authentication.SessionAuthentication',         # Session-based auth
        'rest_framework.authentication.BasicAuthentication',           # Included for compatibility
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'chats.permissions.IsParticipantOfConversation',               # Custom permission class
    ],
}

# Included authentication class: rest_framework.authentication.BasicAuthentication

# JWT-specific settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
