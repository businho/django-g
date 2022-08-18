from django.http import HttpRequest

from . import local


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request: HttpRequest) -> None:
        local._HTTP_REQUEST_VAR.set(request)
