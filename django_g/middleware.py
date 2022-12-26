import django_g


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        django_g.set_request(request)
        try:
            return self.get_response(request)
        finally:
            django_g.set_request(None)
