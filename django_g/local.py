from contextvars import ContextVar
from typing import Optional

from django.http import HttpRequest

_HTTP_REQUEST_VAR: ContextVar[HttpRequest] = ContextVar("http_request", default=None)
