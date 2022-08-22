from contextvars import ContextVar

from django.http import HttpRequest

_HTTP_REQUEST_VAR: ContextVar[HttpRequest] = ContextVar("http_request", default=None)
