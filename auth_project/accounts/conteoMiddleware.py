
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.conf import settings

class LastSeenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.session['last_seen'] = now().isoformat()
