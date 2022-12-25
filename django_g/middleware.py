from django.http import HttpRequest, HttpResponse

import django_g


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request: HttpRequest) -> None:
        django_g.set_request(request)

    def process_response(self, request: HttpRequest, response: HttpResponse) -> None:
        django_g.set_request(None)
