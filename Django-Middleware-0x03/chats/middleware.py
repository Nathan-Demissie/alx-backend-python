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
