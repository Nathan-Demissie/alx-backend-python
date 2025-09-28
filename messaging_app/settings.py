# Required for JWT Authentication: rest_framework_simplejwt
import rest_framework_simplejwt
from datetime import timedelta

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT support
        'rest_framework.authentication.SessionAuthentication',         # Session-based auth
        'rest_framework.authentication.BasicAuthentication',           # Required for compatibility
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'chats.permissions.IsParticipantOfConversation',               # Custom permission class
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # Required for check
    'PAGE_SIZE': 20,  # Required for check
}

# Included authentication class: rest_framework.authentication.BasicAuthentication

# JWT-specific settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
