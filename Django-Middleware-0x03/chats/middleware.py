import logging
from datetime import datetime

# Configure logger to write to requests.log
logger = logging.getLogger("request_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("requests.log")
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_entry)

        response = self.get_response(request)
        return response

from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # Allow access only between 18:00 (6 PM) and 21:00 (9 PM)
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Chat access is restricted outside 6 PM to 9 PM.")

        return self.get_response(request)

from datetime import datetime, timedelta
from django.http import HttpResponseForbidden

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to track requests per IP
        self.ip_message_log = {}

    def __call__(self, request):
        # Only apply rate limiting to POST requests to messaging endpoints
        if request.method == "POST" and request.path.startswith("/api/messages"):
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Initialize or clean up old entries
            if ip not in self.ip_message_log:
                self.ip_message_log[ip] = []
            else:
                # Remove timestamps older than 1 minute
                self.ip_message_log[ip] = [
                    timestamp for timestamp in self.ip_message_log[ip]
                    if now - timestamp < timedelta(minutes=1)
                ]

            # Check if limit exceeded
            if len(self.ip_message_log[ip]) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            # Log current request timestamp
            self.ip_message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        # Get IP from headers or fallback to REMOTE_ADDR
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR", "")

