# Required for JWT Authentication: rest_framework_simplejwt
import rest_framework_simplejwt
from datetime import timedelta

INSTALLED_APPS = [
    ...
    'django_filters',
]
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
    'DEFAULT_PAGINATION_CLASS': 'chats.pagination.MessagePagination',
    'PAGE_SIZE': 20,
}

# rest_framework.authentication.BasicAuthentication

# JWT-specific settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
