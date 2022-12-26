import pytest

from django_g import get_current_request
from django_g.middleware import RequestMiddleware


def test_middleware(mocker):
    def view(request):
        assert request == get_current_request()
        return "OK"

    middleware = RequestMiddleware(view)
    response = middleware(mocker.sentinel.request)
    assert get_current_request() is None
    assert response == "OK"


def test_request_exception_must_cleanup_request_context(mocker):
    def view(request):
        assert request == get_current_request()
        1 / 0

    middleware = RequestMiddleware(view)
    with pytest.raises(ZeroDivisionError):
        middleware(mocker.sentinel.request)

    assert get_current_request() is None


def test_no_current_request():
    assert get_current_request() is None
