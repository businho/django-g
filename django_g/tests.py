from unittest.mock import sentinel

import pytest

from django_g import get_current_request, set_request
from django_g.middleware import RequestMiddleware


@pytest.fixture(autouse=True)
def cleanup():
    yield
    set_request(None)


def test_middleware(mocker):
    middleware = RequestMiddleware(None)
    middleware.process_request(sentinel.request)
    assert get_current_request() == sentinel.request
    middleware.process_response(sentinel.request, sentinel.response)


def test_no_current_request():
    assert get_current_request() is None
