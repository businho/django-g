from typing import Optional

from django.http import HttpRequest

from . import local


def set_request(request: HttpRequest):
    local._HTTP_REQUEST_VAR.set(request)


def get_current_request() -> Optional[HttpRequest]:
    return local._HTTP_REQUEST_VAR.get()
