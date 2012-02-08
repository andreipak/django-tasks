from django.conf import settings
from t3_httplog.models import HttpRequestLogEntry
from datetime import datetime



class HttpRequestDbLoggingMiddleware(object):
    """
    Middleware that stores http requests in the db,
    depending on ENABLE_HTTP_REQUEST_LOGGING setting
    """

    def process_request(self, request):
        if getattr(settings,'ENABLE_HTTP_REQUEST_LOGGING'):
            logentry = HttpRequestLogEntry(
                            date=datetime.now(),
                            request_method=request.META.get('REQUEST_METHOD','?'),
                            path=request.path[:256],
                            query_string=request.META.get('QUERY_STRING','?')[:256]
                        )

            logentry.save()
