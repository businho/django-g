from unittest.mock import sentinel

from django_g import get_current_request
from django_g.middleware import RequestMiddleware


def test_middleware(mocker):
    middleware = RequestMiddleware(None)
    middleware.process_request(sentinel.request)
    assert get_current_request() == sentinel.request
